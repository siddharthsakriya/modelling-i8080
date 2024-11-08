register cycle_count : int = 0

// simply incrementes cycle count
val increment_cycle_count : int -> unit
function increment_cycle_count(count) = {
    cycle_count = cycle_count + count;
}
