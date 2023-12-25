import math
from collections import deque
from itertools import count

input_lines = """
%ls -> cs, jd
%st -> jh, bj
%hc -> tn
%xs -> rr
%pq -> tl, cs
%rj -> km, ck
%lb -> cg
%zz -> dx, ch
%kk -> cs, tc
%hr -> ck, pl
%pj -> cs, pr
%pr -> zl, cs
%tl -> vn, cs
%tc -> cs, hn
&cs -> hn, pj, qb, zl
%lv -> hr
%vn -> cs, ls
&mp -> dr
broadcaster -> ns, pj, xz, sg
%gg -> jh, nx
%cr -> jg, jh
%ch -> dx
&dx -> zj, xz, mp, zn, xs, hc
%fl -> jh, ps
%hn -> pq
%qp -> dx, zj
%bp -> zr
%kl -> lb
%pl -> ck, xq
%rm -> zz, dx
%rz -> jh, fl
%pm -> cs, kk
%zl -> pm
%rk -> ck, kl
&dr -> rx
%cg -> lv, ck
&qt -> dr
%jg -> jh
&qb -> dr
&ck -> lb, lv, ns, kl, qt
%zr -> st
%dd -> dx, qp
%kd -> rk, ck
%xq -> rj, ck
%sg -> rz, jh
%zj -> hc
%tn -> dx, xs
%jd -> cs
%rr -> rm, dx
&jh -> ng, bp, zr, sg, bj
%km -> ck
%ps -> bp, jh
%zn -> dd
%bj -> gg
%nx -> jh, cr
%xz -> dx, zn
&ng -> dr
%ns -> ck, kd
""".strip().splitlines(False)


class CommModule(object):
    _instances: dict[str, "CommModule"] = {}
    pulse_queue = deque()
    low_high_counter = [0, 0]
    recorders: list["RecorderModule"] = []

    def __init__(self, _id: str):
        self.id = _id
        self.destinations = []
        self._instances[_id] = self

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"

    @classmethod
    def get(cls, key):  # create untyped module if it doesn't exist yet
        return cls._instances.get(key) or CommModule(key)

    def start(self):
        for recorder in self.recorders:
            recorder.clear()
        self.send_pulse(False)
        while self.pulse_queue:  # start processing pulses
            self.pulse_queue.popleft()()

    def subscribe(self, source: "CommModule"):
        source.destinations.append(self)

    def send_pulse(self, typ: bool):
        for destination in self.destinations:
            self.low_high_counter[typ] += 1
            self.pulse_queue.append(lambda o=destination: o.process(self.id, typ))

    def process(self, source_id: str, high: bool):
        pass


class BroadcasterModule(CommModule):
    def process(self, source_id: str, high: bool):
        self.send_pulse(high)


class FlipFlopModule(CommModule):
    def __init__(self, _id: str):
        super().__init__(_id)
        self.is_on = False

    def process(self, _, high: bool):
        if not high:
            self.is_on = not self.is_on
            self.send_pulse(self.is_on)


class ConjunctionModule(CommModule):
    def __init__(self, _id: str):
        super().__init__(_id)
        self.inputs: dict[str, bool] = {}

    def subscribe(self, module: CommModule):
        super().subscribe(module)
        self.inputs[module.id] = False

    def process(self, source_id: str, high: bool):
        self.inputs[source_id] = high
        self.send_pulse(not all(self.inputs.values()))
        super().process(source_id, high)


class RecorderModule(CommModule):
    def __init__(self, _id: str):
        super().__init__(_id)
        self.recorders.append(self)
        self.received = []

    def process(self, source_id: str, high: bool):
        self.received.append(high)
        super().process(source_id, high)

    def clear(self):
        self.received.clear()


class ConjunctionRecorder(RecorderModule, ConjunctionModule):
    def __init__(self, _id: str):
        super().__init__(_id)


def initialize_modules():
    config = [(name, dest.split(", ")) for name, dest in map(lambda ln: ln.split(" -> "), input_lines)]
    for n, _ in config:
        if n[0] == "%":
            FlipFlopModule(n[1:])
        # PART 2: For "rx" to receive a low pulse, these four modules must receive a low pulse at the same time:
        elif n[1:] in ["mp", "qt", "qb", "ng"]:
            ConjunctionRecorder(n[1:])
        elif n[0] == "&":
            ConjunctionModule(n[1:])
        else:
            BroadcasterModule(n)
    for n, destinations in config:
        src = CommModule.get(n.lstrip("%&"))
        for destination in destinations:
            CommModule.get(destination).subscribe(src)
    button = CommModule("button")
    CommModule.get("broadcaster").subscribe(button)
    return button


if __name__ == '__main__':
    button_module = initialize_modules()
    loops = {}
    for i in count(1):
        button_module.start()
        if i == 1000:
            print(f"Low/high pulse product after 1000 button presses: {math.prod(CommModule.low_high_counter)}")
        for rec in CommModule.recorders:
            if rec not in loops and not all(rec.received):
                loops[rec.id] = i
        if len(loops) == len(CommModule.recorders):
            print(f"'rx' receives single low pulse after {math.prod(loops.values())} button presses.")
            break
