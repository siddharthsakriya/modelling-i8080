#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#include "sail.h"

void string_hd(sail_int *r, const_sail_string s) {
  mpz_set_ui(*r, s[0]);
}
