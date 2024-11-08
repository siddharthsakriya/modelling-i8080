register clock_cycle_count : int = 0
register machine_cycle_count : int = 0

val increment_clock_cycle_count : int -> unit
function increment_clock_cycle_count(count) = {
    clock_cycle_count = clock_cycle_count + count;
}

val increment_machine_cycle_count : int -> unit
function increment_machine_cycle_count(count) = {
    machine_cycle_count = machine_cycle_count + count
}

