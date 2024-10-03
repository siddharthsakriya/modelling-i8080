#include "sail.h"
#include "rts.h"
#include "elf.h"
#ifdef __cplusplus
extern "C" {
#endif

// enum reg_8bit_enum
enum zreg_8bit_enum { zB, zC, zD, zE, zH, zL, zA, zM };

static bool eq_zreg_8bit_enum(enum zreg_8bit_enum op1, enum zreg_8bit_enum op2) { return op1 == op2; }

static enum zreg_8bit_enum UNDEFINED(zreg_8bit_enum)(unit u) { return zB; }

// enum reg_16bit_enum
enum zreg_16bit_enum { zBC, zDE, zHL, zSP };

static bool eq_zreg_16bit_enum(enum zreg_16bit_enum op1, enum zreg_16bit_enum op2) { return op1 == op2; }

static enum zreg_16bit_enum UNDEFINED(zreg_16bit_enum)(unit u) { return zBC; }

// struct reg16
struct zreg16 {uint64_t zbits;};

static void COPY(zreg16)(struct zreg16 *rop, const struct zreg16 op) {rop->zbits = op.zbits;}

static bool EQUAL(zreg16)(struct zreg16 op1, struct zreg16 op2) {return EQUAL(fbits)(op1.zbits, op2.zbits);}

// struct flag
struct zflag {uint64_t zbits;};

static void COPY(zflag)(struct zflag *rop, const struct zflag op) {rop->zbits = op.zbits;}

static bool EQUAL(zflag)(struct zflag op1, struct zflag op2) {return EQUAL(fbits)(op1.zbits, op2.zbits);}

// union exception
enum kind_zexception { Kind_z__dummy_exnz3 };

struct zexception {
  enum kind_zexception kind;
  union {struct { unit z__dummy_exnz3; };};
};

static void CREATE(zexception)(struct zexception *op)
{
  op->kind = Kind_z__dummy_exnz3;

}

static void RECREATE(zexception)(struct zexception *op) {}

static void KILL(zexception)(struct zexception *op)
{{};}

static void COPY(zexception)(struct zexception *rop, struct zexception op)
{
  {};
  rop->kind = op.kind;
  if (op.kind == Kind_z__dummy_exnz3){
    rop->z__dummy_exnz3 = op.z__dummy_exnz3;
  }
}

static bool EQUAL(zexception)(struct zexception op1, struct zexception op2) {
  if (op1.kind == Kind_z__dummy_exnz3 && op2.kind == Kind_z__dummy_exnz3) {
    return EQUAL(unit)(op1.z__dummy_exnz3, op2.z__dummy_exnz3);
  } else return false;
}

static void z__dummy_exnz3(struct zexception *rop, unit op)
{
  {}
  rop->kind = Kind_z__dummy_exnz3;
  rop->z__dummy_exnz3 = op;
}

struct zexception *current_exception = NULL;
bool have_exception = false;
sail_string *throw_location = NULL;

// union ast
enum kind_zast { Kind_zCMC, Kind_zINR, Kind_zSTC };

struct zast {
  enum kind_zast kind;
  union {
    struct { unit zCMC; };
    struct { uint64_t zINR; };
    struct { unit zSTC; };
  };
};

static void CREATE(zast)(struct zast *op)
{
  op->kind = Kind_zCMC;

}

static void RECREATE(zast)(struct zast *op) {}

static void KILL(zast)(struct zast *op)
{{};}

static void COPY(zast)(struct zast *rop, struct zast op)
{
  {};
  rop->kind = op.kind;
  if (op.kind == Kind_zCMC) {
    rop->zCMC = op.zCMC;
  } else if (op.kind == Kind_zINR) {
    rop->zINR = op.zINR;
  } else if (op.kind == Kind_zSTC){
    rop->zSTC = op.zSTC;
  }
}

static bool EQUAL(zast)(struct zast op1, struct zast op2) {
  if (op1.kind == Kind_zCMC && op2.kind == Kind_zCMC) {
    return EQUAL(unit)(op1.zCMC, op2.zCMC);
  } else if (op1.kind == Kind_zINR && op2.kind == Kind_zINR) {
    return EQUAL(fbits)(op1.zINR, op2.zINR);
  } else if (op1.kind == Kind_zSTC && op2.kind == Kind_zSTC) {
    return EQUAL(unit)(op1.zSTC, op2.zSTC);
  } else return false;
}

static void zCMC(struct zast *rop, unit op)
{
  {}
  rop->kind = Kind_zCMC;
  rop->zCMC = op;
}

static void zINR(struct zast *rop, uint64_t op)
{
  {}
  rop->kind = Kind_zINR;
  rop->zINR = op;
}

static void zSTC(struct zast *rop, unit op)
{
  {}
  rop->kind = Kind_zSTC;
  rop->zSTC = op;
}





















struct zreg16 zundefined_reg16(unit);

struct zreg16 zundefined_reg16(unit zgsz30)
{
  __label__ end_function_1, end_block_exception_2;

  struct zreg16 zcbz30;
  uint64_t zgaz30;
  {
    sail_int zgsz367;
    CREATE(sail_int)(&zgsz367);
    CONVERT_OF(sail_int, mach_int)(&zgsz367, INT64_C(16));
    lbits zgsz368;
    CREATE(lbits)(&zgsz368);
    UNDEFINED(lbits)(&zgsz368, zgsz367);
    zgaz30 = CONVERT_OF(fbits, lbits)(zgsz368, true);
    KILL(lbits)(&zgsz368);
    KILL(sail_int)(&zgsz367);
  }
  struct zreg16 zgsz31;
  zgsz31.zbits = zgaz30;
  zcbz30 = zgsz31;


end_function_1: ;
  return zcbz30;
end_block_exception_2: ;
  struct zreg16 zcbz313 = { .zbits = UINT64_C(0xdeadc0de) };
  return zcbz313;
}

uint64_t z_get_reg16_high(struct zreg16);

uint64_t z_get_reg16_high(struct zreg16 zv)
{
  __label__ end_function_4, end_block_exception_5;

  uint64_t zcbz31;
  uint64_t zgaz31;
  zgaz31 = zv.zbits;
  {
    lbits zgsz369;
    CREATE(lbits)(&zgsz369);
    CONVERT_OF(lbits, fbits)(&zgsz369, zgaz31, UINT64_C(16) , true);
    sail_int zgsz370;
    CREATE(sail_int)(&zgsz370);
    CONVERT_OF(sail_int, mach_int)(&zgsz370, INT64_C(15));
    sail_int zgsz371;
    CREATE(sail_int)(&zgsz371);
    CONVERT_OF(sail_int, mach_int)(&zgsz371, INT64_C(8));
    lbits zgsz372;
    CREATE(lbits)(&zgsz372);
    vector_subrange_lbits(&zgsz372, zgsz369, zgsz370, zgsz371);
    zcbz31 = CONVERT_OF(fbits, lbits)(zgsz372, true);
    KILL(lbits)(&zgsz372);
    KILL(sail_int)(&zgsz371);
    KILL(sail_int)(&zgsz370);
    KILL(lbits)(&zgsz369);
  }

end_function_4: ;
  return zcbz31;
end_block_exception_5: ;

  return UINT64_C(0xdeadc0de);
}

uint64_t z_get_reg16_low(struct zreg16);

uint64_t z_get_reg16_low(struct zreg16 zv)
{
  __label__ end_function_7, end_block_exception_8;

  uint64_t zcbz32;
  uint64_t zgaz32;
  zgaz32 = zv.zbits;
  {
    lbits zgsz373;
    CREATE(lbits)(&zgsz373);
    CONVERT_OF(lbits, fbits)(&zgsz373, zgaz32, UINT64_C(16) , true);
    sail_int zgsz374;
    CREATE(sail_int)(&zgsz374);
    CONVERT_OF(sail_int, mach_int)(&zgsz374, INT64_C(7));
    sail_int zgsz375;
    CREATE(sail_int)(&zgsz375);
    CONVERT_OF(sail_int, mach_int)(&zgsz375, INT64_C(0));
    lbits zgsz376;
    CREATE(lbits)(&zgsz376);
    vector_subrange_lbits(&zgsz376, zgsz373, zgsz374, zgsz375);
    zcbz32 = CONVERT_OF(fbits, lbits)(zgsz376, true);
    KILL(lbits)(&zgsz376);
    KILL(sail_int)(&zgsz375);
    KILL(sail_int)(&zgsz374);
    KILL(lbits)(&zgsz373);
  }

end_function_7: ;
  return zcbz32;
end_block_exception_8: ;

  return UINT64_C(0xdeadc0de);
}

struct zflag zundefined_flag(unit);

struct zflag zundefined_flag(unit zgsz32)
{
  __label__ end_function_10, end_block_exception_11;

  struct zflag zcbz33;
  uint64_t zgaz33;
  {
    sail_int zgsz377;
    CREATE(sail_int)(&zgsz377);
    CONVERT_OF(sail_int, mach_int)(&zgsz377, INT64_C(8));
    lbits zgsz378;
    CREATE(lbits)(&zgsz378);
    UNDEFINED(lbits)(&zgsz378, zgsz377);
    zgaz33 = CONVERT_OF(fbits, lbits)(zgsz378, true);
    KILL(lbits)(&zgsz378);
    KILL(sail_int)(&zgsz377);
  }
  struct zflag zgsz33;
  zgsz33.zbits = zgaz33;
  zcbz33 = zgsz33;


end_function_10: ;
  return zcbz33;
end_block_exception_11: ;
  struct zflag zcbz314 = { .zbits = UINT64_C(0xdeadc0de) };
  return zcbz314;
}

uint64_t z_get_flag_C(struct zflag);

uint64_t z_get_flag_C(struct zflag zv)
{
  __label__ end_function_13, end_block_exception_14;

  uint64_t zcbz34;
  uint64_t zgaz34;
  zgaz34 = zv.zbits;
  {
    lbits zgsz379;
    CREATE(lbits)(&zgsz379);
    CONVERT_OF(lbits, fbits)(&zgsz379, zgaz34, UINT64_C(8) , true);
    sail_int zgsz380;
    CREATE(sail_int)(&zgsz380);
    CONVERT_OF(sail_int, mach_int)(&zgsz380, INT64_C(0));
    sail_int zgsz381;
    CREATE(sail_int)(&zgsz381);
    CONVERT_OF(sail_int, mach_int)(&zgsz381, INT64_C(0));
    lbits zgsz382;
    CREATE(lbits)(&zgsz382);
    vector_subrange_lbits(&zgsz382, zgsz379, zgsz380, zgsz381);
    zcbz34 = CONVERT_OF(fbits, lbits)(zgsz382, true);
    KILL(lbits)(&zgsz382);
    KILL(sail_int)(&zgsz381);
    KILL(sail_int)(&zgsz380);
    KILL(lbits)(&zgsz379);
  }

end_function_13: ;
  return zcbz34;
end_block_exception_14: ;

  return UINT64_C(0xdeadc0de);
}

uint64_t z_get_flag_all(struct zflag);

uint64_t z_get_flag_all(struct zflag zv)
{
  __label__ end_function_16, end_block_exception_17;

  uint64_t zcbz35;
  uint64_t zgaz35;
  zgaz35 = zv.zbits;
  {
    lbits zgsz383;
    CREATE(lbits)(&zgsz383);
    CONVERT_OF(lbits, fbits)(&zgsz383, zgaz35, UINT64_C(8) , true);
    sail_int zgsz384;
    CREATE(sail_int)(&zgsz384);
    CONVERT_OF(sail_int, mach_int)(&zgsz384, INT64_C(7));
    sail_int zgsz385;
    CREATE(sail_int)(&zgsz385);
    CONVERT_OF(sail_int, mach_int)(&zgsz385, INT64_C(0));
    lbits zgsz386;
    CREATE(lbits)(&zgsz386);
    vector_subrange_lbits(&zgsz386, zgsz383, zgsz384, zgsz385);
    zcbz35 = CONVERT_OF(fbits, lbits)(zgsz386, true);
    KILL(lbits)(&zgsz386);
    KILL(sail_int)(&zgsz385);
    KILL(sail_int)(&zgsz384);
    KILL(lbits)(&zgsz383);
  }

end_function_16: ;
  return zcbz35;
end_block_exception_17: ;

  return UINT64_C(0xdeadc0de);
}

// register A_reg
uint64_t zA_reg;

// register SFW_reg
struct zflag zSFW_reg;

// register BC_reg
struct zreg16 zBC_reg;

// register DE_reg
struct zreg16 zDE_reg;

// register HL_reg
struct zreg16 zHL_reg;

// register SP_reg
struct zreg16 zSP_reg;

uint64_t zxor_reduce(uint64_t);

uint64_t zxor_reduce(uint64_t zv)
{
  __label__ end_function_21, end_block_exception_22;

  uint64_t zcbz36;
  uint64_t zx;
  {
    fbits zgaz37;
    {
      lbits zgsz387;
      CREATE(lbits)(&zgsz387);
      CONVERT_OF(lbits, fbits)(&zgsz387, zv, UINT64_C(8) , true);
      sail_int zgsz388;
      CREATE(sail_int)(&zgsz388);
      CONVERT_OF(sail_int, mach_int)(&zgsz388, INT64_C(0));
      zgaz37 = bitvector_access(zgsz387, zgsz388);
      KILL(sail_int)(&zgsz388);
      KILL(lbits)(&zgsz387);
    }
    uint64_t zgsz34;
    zgsz34 = UINT64_C(0b0);
    zgsz34 = update_fbits(zgsz34, INT64_C(0), zgaz37);
    zx = zgsz34;
  }
  {
    int64_t zgsz35;
    {    zgsz35 = INT64_C(1);
    }
    int64_t zgsz36;
    {    zgsz36 = INT64_C(7);
    }
    int64_t zgsz37;
    {    zgsz37 = INT64_C(1);
    }
    {
      __label__ for_start_19, for_end_20;

      int64_t zi;
      zi = zgsz35;
      unit zgsz39;
    for_start_19: ;
      {
        if ((zi > zgsz36)) goto for_end_20;
        uint64_t zy;
        zy = zx;
        uint64_t zzz;
        {
          fbits zgaz36;
          {
            lbits zgsz389;
            CREATE(lbits)(&zgsz389);
            CONVERT_OF(lbits, fbits)(&zgsz389, zv, UINT64_C(8) , true);
            sail_int zgsz390;
            CREATE(sail_int)(&zgsz390);
            CONVERT_OF(sail_int, mach_int)(&zgsz390, zi);
            zgaz36 = bitvector_access(zgsz389, zgsz390);
            KILL(sail_int)(&zgsz390);
            KILL(lbits)(&zgsz389);
          }
          uint64_t zgsz38;
          zgsz38 = UINT64_C(0b0);
          zgsz38 = update_fbits(zgsz38, INT64_C(0), zgaz36);
          zzz = zgsz38;
        }
        {
          lbits zgsz391;
          CREATE(lbits)(&zgsz391);
          CONVERT_OF(lbits, fbits)(&zgsz391, zy, UINT64_C(1) , true);
          lbits zgsz392;
          CREATE(lbits)(&zgsz392);
          CONVERT_OF(lbits, fbits)(&zgsz392, zzz, UINT64_C(1) , true);
          lbits zgsz393;
          CREATE(lbits)(&zgsz393);
          xor_bits(&zgsz393, zgsz391, zgsz392);
          zx = CONVERT_OF(fbits, lbits)(zgsz393, true);
          KILL(lbits)(&zgsz393);
          KILL(lbits)(&zgsz392);
          KILL(lbits)(&zgsz391);
        }
        zgsz39 = UNIT;
        zi = (zi + zgsz37);
        goto for_start_19;
      }
    for_end_20: ;
    }
    unit zgsz310;
    zgsz310 = UNIT;
  }
  zcbz36 = zx;

end_function_21: ;
  return zcbz36;
end_block_exception_22: ;

  return UINT64_C(0xdeadc0de);
}

uint64_t zread_reg8(uint64_t);

uint64_t zread_reg8(uint64_t zr)
{
  __label__ case_25, case_26, case_27, case_28, case_29, case_30, case_31, finish_match_24, end_function_32, end_block_exception_33;

  uint64_t zcbz37;
  /* Case with num_cases: 7 */
  uint64_t zgsz311;
  {
    uint64_t zb__0;
    zb__0 = zr;
    bool zgsz312;
    {
      lbits zgsz394;
      CREATE(lbits)(&zgsz394);
      CONVERT_OF(lbits, fbits)(&zgsz394, zb__0, UINT64_C(3) , true);
      lbits zgsz395;
      CREATE(lbits)(&zgsz395);
      CONVERT_OF(lbits, fbits)(&zgsz395, UINT64_C(0b000), UINT64_C(3) , true);
      zgsz312 = eq_bits(zgsz394, zgsz395);
      KILL(lbits)(&zgsz395);
      KILL(lbits)(&zgsz394);
    }
    if (!(zgsz312)) {

      goto case_25;
    }
    zgsz311 = z_get_reg16_high(zBC_reg);
    goto finish_match_24;
  }
case_25: ;
  {
    uint64_t zb__1;
    zb__1 = zr;
    bool zgsz313;
    {
      lbits zgsz396;
      CREATE(lbits)(&zgsz396);
      CONVERT_OF(lbits, fbits)(&zgsz396, zb__1, UINT64_C(3) , true);
      lbits zgsz397;
      CREATE(lbits)(&zgsz397);
      CONVERT_OF(lbits, fbits)(&zgsz397, UINT64_C(0b001), UINT64_C(3) , true);
      zgsz313 = eq_bits(zgsz396, zgsz397);
      KILL(lbits)(&zgsz397);
      KILL(lbits)(&zgsz396);
    }
    if (!(zgsz313)) {

      goto case_26;
    }
    zgsz311 = z_get_reg16_low(zBC_reg);
    goto finish_match_24;
  }
case_26: ;
  {
    uint64_t zb__2;
    zb__2 = zr;
    bool zgsz314;
    {
      lbits zgsz398;
      CREATE(lbits)(&zgsz398);
      CONVERT_OF(lbits, fbits)(&zgsz398, zb__2, UINT64_C(3) , true);
      lbits zgsz399;
      CREATE(lbits)(&zgsz399);
      CONVERT_OF(lbits, fbits)(&zgsz399, UINT64_C(0b010), UINT64_C(3) , true);
      zgsz314 = eq_bits(zgsz398, zgsz399);
      KILL(lbits)(&zgsz399);
      KILL(lbits)(&zgsz398);
    }
    if (!(zgsz314)) {

      goto case_27;
    }
    zgsz311 = z_get_reg16_high(zDE_reg);
    goto finish_match_24;
  }
case_27: ;
  {
    uint64_t zb__3;
    zb__3 = zr;
    bool zgsz315;
    {
      lbits zgsz3100;
      CREATE(lbits)(&zgsz3100);
      CONVERT_OF(lbits, fbits)(&zgsz3100, zb__3, UINT64_C(3) , true);
      lbits zgsz3101;
      CREATE(lbits)(&zgsz3101);
      CONVERT_OF(lbits, fbits)(&zgsz3101, UINT64_C(0b011), UINT64_C(3) , true);
      zgsz315 = eq_bits(zgsz3100, zgsz3101);
      KILL(lbits)(&zgsz3101);
      KILL(lbits)(&zgsz3100);
    }
    if (!(zgsz315)) {

      goto case_28;
    }
    zgsz311 = z_get_reg16_low(zDE_reg);
    goto finish_match_24;
  }
case_28: ;
  {
    uint64_t zb__4;
    zb__4 = zr;
    bool zgsz316;
    {
      lbits zgsz3102;
      CREATE(lbits)(&zgsz3102);
      CONVERT_OF(lbits, fbits)(&zgsz3102, zb__4, UINT64_C(3) , true);
      lbits zgsz3103;
      CREATE(lbits)(&zgsz3103);
      CONVERT_OF(lbits, fbits)(&zgsz3103, UINT64_C(0b100), UINT64_C(3) , true);
      zgsz316 = eq_bits(zgsz3102, zgsz3103);
      KILL(lbits)(&zgsz3103);
      KILL(lbits)(&zgsz3102);
    }
    if (!(zgsz316)) {

      goto case_29;
    }
    zgsz311 = z_get_reg16_high(zHL_reg);
    goto finish_match_24;
  }
case_29: ;
  {
    uint64_t zb__5;
    zb__5 = zr;
    bool zgsz317;
    {
      lbits zgsz3104;
      CREATE(lbits)(&zgsz3104);
      CONVERT_OF(lbits, fbits)(&zgsz3104, zb__5, UINT64_C(3) , true);
      lbits zgsz3105;
      CREATE(lbits)(&zgsz3105);
      CONVERT_OF(lbits, fbits)(&zgsz3105, UINT64_C(0b101), UINT64_C(3) , true);
      zgsz317 = eq_bits(zgsz3104, zgsz3105);
      KILL(lbits)(&zgsz3105);
      KILL(lbits)(&zgsz3104);
    }
    if (!(zgsz317)) {

      goto case_30;
    }
    zgsz311 = z_get_reg16_low(zHL_reg);
    goto finish_match_24;
  }
case_30: ;
  {
    uint64_t zb__6;
    zb__6 = zr;
    bool zgsz318;
    {
      lbits zgsz3106;
      CREATE(lbits)(&zgsz3106);
      CONVERT_OF(lbits, fbits)(&zgsz3106, zb__6, UINT64_C(3) , true);
      lbits zgsz3107;
      CREATE(lbits)(&zgsz3107);
      CONVERT_OF(lbits, fbits)(&zgsz3107, UINT64_C(0b111), UINT64_C(3) , true);
      zgsz318 = eq_bits(zgsz3106, zgsz3107);
      KILL(lbits)(&zgsz3107);
      KILL(lbits)(&zgsz3106);
    }
    if (!(zgsz318)) {

      goto case_31;
    }
    zgsz311 = zA_reg;
    goto finish_match_24;
  }
case_31: ;
  sail_match_failure("read_reg8");
finish_match_24: ;
  zcbz37 = zgsz311;

end_function_32: ;
  return zcbz37;
end_block_exception_33: ;

  return UINT64_C(0xdeadc0de);
}

unit zwrite_reg8(uint64_t, uint64_t);

unit zwrite_reg8(uint64_t zr, uint64_t zv)
{
  __label__ case_36, case_37, case_38, case_39, case_40, case_41, case_42, finish_match_35, end_function_43, end_block_exception_44;

  unit zcbz38;
  /* Case with num_cases: 7 */
  unit zgsz319;
  {
    uint64_t zb__0;
    zb__0 = zr;
    bool zgsz321;
    {
      lbits zgsz3113;
      CREATE(lbits)(&zgsz3113);
      CONVERT_OF(lbits, fbits)(&zgsz3113, zb__0, UINT64_C(3) , true);
      lbits zgsz3114;
      CREATE(lbits)(&zgsz3114);
      CONVERT_OF(lbits, fbits)(&zgsz3114, UINT64_C(0b000), UINT64_C(3) , true);
      zgsz321 = eq_bits(zgsz3113, zgsz3114);
      KILL(lbits)(&zgsz3114);
      KILL(lbits)(&zgsz3113);
    }
    if (!(zgsz321)) {

      goto case_36;
    }
    uint64_t zgaz39;
    {
      uint64_t zgaz38;
      zgaz38 = zBC_reg.zbits;
      {
        lbits zgsz3108;
        CREATE(lbits)(&zgsz3108);
        CONVERT_OF(lbits, fbits)(&zgsz3108, zgaz38, UINT64_C(16) , true);
        sail_int zgsz3109;
        CREATE(sail_int)(&zgsz3109);
        CONVERT_OF(sail_int, mach_int)(&zgsz3109, INT64_C(15));
        sail_int zgsz3110;
        CREATE(sail_int)(&zgsz3110);
        CONVERT_OF(sail_int, mach_int)(&zgsz3110, INT64_C(8));
        lbits zgsz3111;
        CREATE(lbits)(&zgsz3111);
        CONVERT_OF(lbits, fbits)(&zgsz3111, zv, UINT64_C(8) , true);
        lbits zgsz3112;
        CREATE(lbits)(&zgsz3112);
        vector_update_subrange_lbits(&zgsz3112, zgsz3108, zgsz3109, zgsz3110, zgsz3111);
        zgaz39 = CONVERT_OF(fbits, lbits)(zgsz3112, true);
        KILL(lbits)(&zgsz3112);
        KILL(lbits)(&zgsz3111);
        KILL(sail_int)(&zgsz3110);
        KILL(sail_int)(&zgsz3109);
        KILL(lbits)(&zgsz3108);
      }
    }
    struct zreg16 zgsz320;
    zgsz320 = zBC_reg;
    zgsz320.zbits = zgaz39;
    zBC_reg = zgsz320;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_36: ;
  {
    uint64_t zb__1;
    zb__1 = zr;
    bool zgsz323;
    {
      lbits zgsz3120;
      CREATE(lbits)(&zgsz3120);
      CONVERT_OF(lbits, fbits)(&zgsz3120, zb__1, UINT64_C(3) , true);
      lbits zgsz3121;
      CREATE(lbits)(&zgsz3121);
      CONVERT_OF(lbits, fbits)(&zgsz3121, UINT64_C(0b001), UINT64_C(3) , true);
      zgsz323 = eq_bits(zgsz3120, zgsz3121);
      KILL(lbits)(&zgsz3121);
      KILL(lbits)(&zgsz3120);
    }
    if (!(zgsz323)) {

      goto case_37;
    }
    uint64_t zgaz311;
    {
      uint64_t zgaz310;
      zgaz310 = zBC_reg.zbits;
      {
        lbits zgsz3115;
        CREATE(lbits)(&zgsz3115);
        CONVERT_OF(lbits, fbits)(&zgsz3115, zgaz310, UINT64_C(16) , true);
        sail_int zgsz3116;
        CREATE(sail_int)(&zgsz3116);
        CONVERT_OF(sail_int, mach_int)(&zgsz3116, INT64_C(7));
        sail_int zgsz3117;
        CREATE(sail_int)(&zgsz3117);
        CONVERT_OF(sail_int, mach_int)(&zgsz3117, INT64_C(0));
        lbits zgsz3118;
        CREATE(lbits)(&zgsz3118);
        CONVERT_OF(lbits, fbits)(&zgsz3118, zv, UINT64_C(8) , true);
        lbits zgsz3119;
        CREATE(lbits)(&zgsz3119);
        vector_update_subrange_lbits(&zgsz3119, zgsz3115, zgsz3116, zgsz3117, zgsz3118);
        zgaz311 = CONVERT_OF(fbits, lbits)(zgsz3119, true);
        KILL(lbits)(&zgsz3119);
        KILL(lbits)(&zgsz3118);
        KILL(sail_int)(&zgsz3117);
        KILL(sail_int)(&zgsz3116);
        KILL(lbits)(&zgsz3115);
      }
    }
    struct zreg16 zgsz322;
    zgsz322 = zBC_reg;
    zgsz322.zbits = zgaz311;
    zBC_reg = zgsz322;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_37: ;
  {
    uint64_t zb__2;
    zb__2 = zr;
    bool zgsz325;
    {
      lbits zgsz3127;
      CREATE(lbits)(&zgsz3127);
      CONVERT_OF(lbits, fbits)(&zgsz3127, zb__2, UINT64_C(3) , true);
      lbits zgsz3128;
      CREATE(lbits)(&zgsz3128);
      CONVERT_OF(lbits, fbits)(&zgsz3128, UINT64_C(0b010), UINT64_C(3) , true);
      zgsz325 = eq_bits(zgsz3127, zgsz3128);
      KILL(lbits)(&zgsz3128);
      KILL(lbits)(&zgsz3127);
    }
    if (!(zgsz325)) {

      goto case_38;
    }
    uint64_t zgaz313;
    {
      uint64_t zgaz312;
      zgaz312 = zDE_reg.zbits;
      {
        lbits zgsz3122;
        CREATE(lbits)(&zgsz3122);
        CONVERT_OF(lbits, fbits)(&zgsz3122, zgaz312, UINT64_C(16) , true);
        sail_int zgsz3123;
        CREATE(sail_int)(&zgsz3123);
        CONVERT_OF(sail_int, mach_int)(&zgsz3123, INT64_C(15));
        sail_int zgsz3124;
        CREATE(sail_int)(&zgsz3124);
        CONVERT_OF(sail_int, mach_int)(&zgsz3124, INT64_C(8));
        lbits zgsz3125;
        CREATE(lbits)(&zgsz3125);
        CONVERT_OF(lbits, fbits)(&zgsz3125, zv, UINT64_C(8) , true);
        lbits zgsz3126;
        CREATE(lbits)(&zgsz3126);
        vector_update_subrange_lbits(&zgsz3126, zgsz3122, zgsz3123, zgsz3124, zgsz3125);
        zgaz313 = CONVERT_OF(fbits, lbits)(zgsz3126, true);
        KILL(lbits)(&zgsz3126);
        KILL(lbits)(&zgsz3125);
        KILL(sail_int)(&zgsz3124);
        KILL(sail_int)(&zgsz3123);
        KILL(lbits)(&zgsz3122);
      }
    }
    struct zreg16 zgsz324;
    zgsz324 = zDE_reg;
    zgsz324.zbits = zgaz313;
    zDE_reg = zgsz324;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_38: ;
  {
    uint64_t zb__3;
    zb__3 = zr;
    bool zgsz327;
    {
      lbits zgsz3134;
      CREATE(lbits)(&zgsz3134);
      CONVERT_OF(lbits, fbits)(&zgsz3134, zb__3, UINT64_C(3) , true);
      lbits zgsz3135;
      CREATE(lbits)(&zgsz3135);
      CONVERT_OF(lbits, fbits)(&zgsz3135, UINT64_C(0b011), UINT64_C(3) , true);
      zgsz327 = eq_bits(zgsz3134, zgsz3135);
      KILL(lbits)(&zgsz3135);
      KILL(lbits)(&zgsz3134);
    }
    if (!(zgsz327)) {

      goto case_39;
    }
    uint64_t zgaz315;
    {
      uint64_t zgaz314;
      zgaz314 = zDE_reg.zbits;
      {
        lbits zgsz3129;
        CREATE(lbits)(&zgsz3129);
        CONVERT_OF(lbits, fbits)(&zgsz3129, zgaz314, UINT64_C(16) , true);
        sail_int zgsz3130;
        CREATE(sail_int)(&zgsz3130);
        CONVERT_OF(sail_int, mach_int)(&zgsz3130, INT64_C(7));
        sail_int zgsz3131;
        CREATE(sail_int)(&zgsz3131);
        CONVERT_OF(sail_int, mach_int)(&zgsz3131, INT64_C(0));
        lbits zgsz3132;
        CREATE(lbits)(&zgsz3132);
        CONVERT_OF(lbits, fbits)(&zgsz3132, zv, UINT64_C(8) , true);
        lbits zgsz3133;
        CREATE(lbits)(&zgsz3133);
        vector_update_subrange_lbits(&zgsz3133, zgsz3129, zgsz3130, zgsz3131, zgsz3132);
        zgaz315 = CONVERT_OF(fbits, lbits)(zgsz3133, true);
        KILL(lbits)(&zgsz3133);
        KILL(lbits)(&zgsz3132);
        KILL(sail_int)(&zgsz3131);
        KILL(sail_int)(&zgsz3130);
        KILL(lbits)(&zgsz3129);
      }
    }
    struct zreg16 zgsz326;
    zgsz326 = zDE_reg;
    zgsz326.zbits = zgaz315;
    zDE_reg = zgsz326;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_39: ;
  {
    uint64_t zb__4;
    zb__4 = zr;
    bool zgsz329;
    {
      lbits zgsz3141;
      CREATE(lbits)(&zgsz3141);
      CONVERT_OF(lbits, fbits)(&zgsz3141, zb__4, UINT64_C(3) , true);
      lbits zgsz3142;
      CREATE(lbits)(&zgsz3142);
      CONVERT_OF(lbits, fbits)(&zgsz3142, UINT64_C(0b100), UINT64_C(3) , true);
      zgsz329 = eq_bits(zgsz3141, zgsz3142);
      KILL(lbits)(&zgsz3142);
      KILL(lbits)(&zgsz3141);
    }
    if (!(zgsz329)) {

      goto case_40;
    }
    uint64_t zgaz317;
    {
      uint64_t zgaz316;
      zgaz316 = zHL_reg.zbits;
      {
        lbits zgsz3136;
        CREATE(lbits)(&zgsz3136);
        CONVERT_OF(lbits, fbits)(&zgsz3136, zgaz316, UINT64_C(16) , true);
        sail_int zgsz3137;
        CREATE(sail_int)(&zgsz3137);
        CONVERT_OF(sail_int, mach_int)(&zgsz3137, INT64_C(15));
        sail_int zgsz3138;
        CREATE(sail_int)(&zgsz3138);
        CONVERT_OF(sail_int, mach_int)(&zgsz3138, INT64_C(8));
        lbits zgsz3139;
        CREATE(lbits)(&zgsz3139);
        CONVERT_OF(lbits, fbits)(&zgsz3139, zv, UINT64_C(8) , true);
        lbits zgsz3140;
        CREATE(lbits)(&zgsz3140);
        vector_update_subrange_lbits(&zgsz3140, zgsz3136, zgsz3137, zgsz3138, zgsz3139);
        zgaz317 = CONVERT_OF(fbits, lbits)(zgsz3140, true);
        KILL(lbits)(&zgsz3140);
        KILL(lbits)(&zgsz3139);
        KILL(sail_int)(&zgsz3138);
        KILL(sail_int)(&zgsz3137);
        KILL(lbits)(&zgsz3136);
      }
    }
    struct zreg16 zgsz328;
    zgsz328 = zHL_reg;
    zgsz328.zbits = zgaz317;
    zHL_reg = zgsz328;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_40: ;
  {
    uint64_t zb__5;
    zb__5 = zr;
    bool zgsz331;
    {
      lbits zgsz3148;
      CREATE(lbits)(&zgsz3148);
      CONVERT_OF(lbits, fbits)(&zgsz3148, zb__5, UINT64_C(3) , true);
      lbits zgsz3149;
      CREATE(lbits)(&zgsz3149);
      CONVERT_OF(lbits, fbits)(&zgsz3149, UINT64_C(0b101), UINT64_C(3) , true);
      zgsz331 = eq_bits(zgsz3148, zgsz3149);
      KILL(lbits)(&zgsz3149);
      KILL(lbits)(&zgsz3148);
    }
    if (!(zgsz331)) {

      goto case_41;
    }
    uint64_t zgaz319;
    {
      uint64_t zgaz318;
      zgaz318 = zHL_reg.zbits;
      {
        lbits zgsz3143;
        CREATE(lbits)(&zgsz3143);
        CONVERT_OF(lbits, fbits)(&zgsz3143, zgaz318, UINT64_C(16) , true);
        sail_int zgsz3144;
        CREATE(sail_int)(&zgsz3144);
        CONVERT_OF(sail_int, mach_int)(&zgsz3144, INT64_C(7));
        sail_int zgsz3145;
        CREATE(sail_int)(&zgsz3145);
        CONVERT_OF(sail_int, mach_int)(&zgsz3145, INT64_C(0));
        lbits zgsz3146;
        CREATE(lbits)(&zgsz3146);
        CONVERT_OF(lbits, fbits)(&zgsz3146, zv, UINT64_C(8) , true);
        lbits zgsz3147;
        CREATE(lbits)(&zgsz3147);
        vector_update_subrange_lbits(&zgsz3147, zgsz3143, zgsz3144, zgsz3145, zgsz3146);
        zgaz319 = CONVERT_OF(fbits, lbits)(zgsz3147, true);
        KILL(lbits)(&zgsz3147);
        KILL(lbits)(&zgsz3146);
        KILL(sail_int)(&zgsz3145);
        KILL(sail_int)(&zgsz3144);
        KILL(lbits)(&zgsz3143);
      }
    }
    struct zreg16 zgsz330;
    zgsz330 = zHL_reg;
    zgsz330.zbits = zgaz319;
    zHL_reg = zgsz330;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_41: ;
  {
    uint64_t zb__6;
    zb__6 = zr;
    bool zgsz332;
    {
      lbits zgsz3150;
      CREATE(lbits)(&zgsz3150);
      CONVERT_OF(lbits, fbits)(&zgsz3150, zb__6, UINT64_C(3) , true);
      lbits zgsz3151;
      CREATE(lbits)(&zgsz3151);
      CONVERT_OF(lbits, fbits)(&zgsz3151, UINT64_C(0b111), UINT64_C(3) , true);
      zgsz332 = eq_bits(zgsz3150, zgsz3151);
      KILL(lbits)(&zgsz3151);
      KILL(lbits)(&zgsz3150);
    }
    if (!(zgsz332)) {

      goto case_42;
    }
    zA_reg = zv;
    zgsz319 = UNIT;
    goto finish_match_35;
  }
case_42: ;
  sail_match_failure("write_reg8");
finish_match_35: ;
  zcbz38 = zgsz319;

end_function_43: ;
  return zcbz38;
end_block_exception_44: ;

  return UNIT;
}

void zdecode8(struct zast *rop, uint64_t);

void zdecode8(struct zast *zcbz39, uint64_t zmergez3var)
{
  __label__ case_47, case_48, case_49, finish_match_46, end_function_50, end_block_exception_51, end_function_65;

  /* Case with num_cases: 3 */
  struct zast zgsz333;
  CREATE(zast)(&zgsz333);
  {
    uint64_t zb__0;
    zb__0 = zmergez3var;
    bool zgsz334;
    {
      lbits zgsz3152;
      CREATE(lbits)(&zgsz3152);
      CONVERT_OF(lbits, fbits)(&zgsz3152, zb__0, UINT64_C(8) , true);
      lbits zgsz3153;
      CREATE(lbits)(&zgsz3153);
      CONVERT_OF(lbits, fbits)(&zgsz3153, UINT64_C(0x3F), UINT64_C(8) , true);
      zgsz334 = eq_bits(zgsz3152, zgsz3153);
      KILL(lbits)(&zgsz3153);
      KILL(lbits)(&zgsz3152);
    }
    if (!(zgsz334)) {

      goto case_47;
    }
    zCMC(&zgsz333, UNIT);
    goto finish_match_46;
  }
case_47: ;
  {
    uint64_t zb__1;
    zb__1 = zmergez3var;
    bool zgsz335;
    {
      lbits zgsz3154;
      CREATE(lbits)(&zgsz3154);
      CONVERT_OF(lbits, fbits)(&zgsz3154, zb__1, UINT64_C(8) , true);
      lbits zgsz3155;
      CREATE(lbits)(&zgsz3155);
      CONVERT_OF(lbits, fbits)(&zgsz3155, UINT64_C(0x37), UINT64_C(8) , true);
      zgsz335 = eq_bits(zgsz3154, zgsz3155);
      KILL(lbits)(&zgsz3155);
      KILL(lbits)(&zgsz3154);
    }
    if (!(zgsz335)) {

      goto case_48;
    }
    zSTC(&zgsz333, UNIT);
    goto finish_match_46;
  }
case_48: ;
  {
    uint64_t zv__0;
    zv__0 = zmergez3var;
    bool zgaz322;
    {
      uint64_t zgaz320;
      {
        lbits zgsz3158;
        CREATE(lbits)(&zgsz3158);
        CONVERT_OF(lbits, fbits)(&zgsz3158, zv__0, UINT64_C(8) , true);
        sail_int zgsz3159;
        CREATE(sail_int)(&zgsz3159);
        CONVERT_OF(sail_int, mach_int)(&zgsz3159, INT64_C(7));
        sail_int zgsz3160;
        CREATE(sail_int)(&zgsz3160);
        CONVERT_OF(sail_int, mach_int)(&zgsz3160, INT64_C(6));
        lbits zgsz3161;
        CREATE(lbits)(&zgsz3161);
        vector_subrange_lbits(&zgsz3161, zgsz3158, zgsz3159, zgsz3160);
        zgaz320 = CONVERT_OF(fbits, lbits)(zgsz3161, true);
        KILL(lbits)(&zgsz3161);
        KILL(sail_int)(&zgsz3160);
        KILL(sail_int)(&zgsz3159);
        KILL(lbits)(&zgsz3158);
      }
      {
        lbits zgsz3156;
        CREATE(lbits)(&zgsz3156);
        CONVERT_OF(lbits, fbits)(&zgsz3156, zgaz320, UINT64_C(2) , true);
        lbits zgsz3157;
        CREATE(lbits)(&zgsz3157);
        CONVERT_OF(lbits, fbits)(&zgsz3157, UINT64_C(0b00), UINT64_C(2) , true);
        zgaz322 = eq_bits(zgsz3156, zgsz3157);
        KILL(lbits)(&zgsz3157);
        KILL(lbits)(&zgsz3156);
      }
    }
    bool zgsz336;
    if (zgaz322) {
      uint64_t zgaz321;
      {
        lbits zgsz3164;
        CREATE(lbits)(&zgsz3164);
        CONVERT_OF(lbits, fbits)(&zgsz3164, zv__0, UINT64_C(8) , true);
        sail_int zgsz3165;
        CREATE(sail_int)(&zgsz3165);
        CONVERT_OF(sail_int, mach_int)(&zgsz3165, INT64_C(2));
        sail_int zgsz3166;
        CREATE(sail_int)(&zgsz3166);
        CONVERT_OF(sail_int, mach_int)(&zgsz3166, INT64_C(0));
        lbits zgsz3167;
        CREATE(lbits)(&zgsz3167);
        vector_subrange_lbits(&zgsz3167, zgsz3164, zgsz3165, zgsz3166);
        zgaz321 = CONVERT_OF(fbits, lbits)(zgsz3167, true);
        KILL(lbits)(&zgsz3167);
        KILL(sail_int)(&zgsz3166);
        KILL(sail_int)(&zgsz3165);
        KILL(lbits)(&zgsz3164);
      }
      {
        lbits zgsz3162;
        CREATE(lbits)(&zgsz3162);
        CONVERT_OF(lbits, fbits)(&zgsz3162, zgaz321, UINT64_C(3) , true);
        lbits zgsz3163;
        CREATE(lbits)(&zgsz3163);
        CONVERT_OF(lbits, fbits)(&zgsz3163, UINT64_C(0b100), UINT64_C(3) , true);
        zgsz336 = eq_bits(zgsz3162, zgsz3163);
        KILL(lbits)(&zgsz3163);
        KILL(lbits)(&zgsz3162);
      }
    } else {  zgsz336 = false;  }
    bool zgsz337;
    zgsz337 = zgsz336;
    if (!(zgsz337)) {

      goto case_49;
    }
    uint64_t zr;
    {
      lbits zgsz3168;
      CREATE(lbits)(&zgsz3168);
      CONVERT_OF(lbits, fbits)(&zgsz3168, zv__0, UINT64_C(8) , true);
      sail_int zgsz3169;
      CREATE(sail_int)(&zgsz3169);
      CONVERT_OF(sail_int, mach_int)(&zgsz3169, INT64_C(5));
      sail_int zgsz3170;
      CREATE(sail_int)(&zgsz3170);
      CONVERT_OF(sail_int, mach_int)(&zgsz3170, INT64_C(3));
      lbits zgsz3171;
      CREATE(lbits)(&zgsz3171);
      vector_subrange_lbits(&zgsz3171, zgsz3168, zgsz3169, zgsz3170);
      zr = CONVERT_OF(fbits, lbits)(zgsz3171, true);
      KILL(lbits)(&zgsz3171);
      KILL(sail_int)(&zgsz3170);
      KILL(sail_int)(&zgsz3169);
      KILL(lbits)(&zgsz3168);
    }
    zINR(&zgsz333, zr);
    goto finish_match_46;
  }
case_49: ;
  sail_match_failure("decode8");
finish_match_46: ;
  COPY(zast)((*(&zcbz39)), zgsz333);
  KILL(zast)(&zgsz333);
end_function_50: ;
  goto end_function_65;
end_block_exception_51: ;
  goto end_function_65;
end_function_65: ;
}

bool zexecute(struct zast);

bool zexecute(struct zast zmergez3var)
{
  __label__ case_54, case_55, case_56, finish_match_53, end_function_57, end_block_exception_58;

  bool zcbz310;
  /* Case with num_cases: 3 */
  bool zgsz338;
  {
    if (zmergez3var.kind != Kind_zCMC) goto case_54;
    {
      uint64_t zgaz327;
      {
        uint64_t zgaz325;
        zgaz325 = zSFW_reg.zbits;
        uint64_t zgaz326;
        {
          bool zgaz324;
          {
            uint64_t zgaz323;
            zgaz323 = z_get_flag_C(zSFW_reg);
            {
              lbits zgsz3172;
              CREATE(lbits)(&zgsz3172);
              CONVERT_OF(lbits, fbits)(&zgsz3172, zgaz323, UINT64_C(1) , true);
              lbits zgsz3173;
              CREATE(lbits)(&zgsz3173);
              CONVERT_OF(lbits, fbits)(&zgsz3173, UINT64_C(0b1), UINT64_C(1) , true);
              zgaz324 = eq_bits(zgsz3172, zgsz3173);
              KILL(lbits)(&zgsz3173);
              KILL(lbits)(&zgsz3172);
            }
          }
          if (zgaz324) {  zgaz326 = UINT64_C(0b0);  } else {  zgaz326 = UINT64_C(0b1);  }
        }
        {
          lbits zgsz3174;
          CREATE(lbits)(&zgsz3174);
          CONVERT_OF(lbits, fbits)(&zgsz3174, zgaz325, UINT64_C(8) , true);
          sail_int zgsz3175;
          CREATE(sail_int)(&zgsz3175);
          CONVERT_OF(sail_int, mach_int)(&zgsz3175, INT64_C(0));
          sail_int zgsz3176;
          CREATE(sail_int)(&zgsz3176);
          CONVERT_OF(sail_int, mach_int)(&zgsz3176, INT64_C(0));
          lbits zgsz3177;
          CREATE(lbits)(&zgsz3177);
          CONVERT_OF(lbits, fbits)(&zgsz3177, zgaz326, UINT64_C(1) , true);
          lbits zgsz3178;
          CREATE(lbits)(&zgsz3178);
          vector_update_subrange_lbits(&zgsz3178, zgsz3174, zgsz3175, zgsz3176, zgsz3177);
          zgaz327 = CONVERT_OF(fbits, lbits)(zgsz3178, true);
          KILL(lbits)(&zgsz3178);
          KILL(lbits)(&zgsz3177);
          KILL(sail_int)(&zgsz3176);
          KILL(sail_int)(&zgsz3175);
          KILL(lbits)(&zgsz3174);
        }
      }
      struct zflag zgsz339;
      zgsz339 = zSFW_reg;
      zgsz339.zbits = zgaz327;
      zSFW_reg = zgsz339;
      unit zgsz340;
      zgsz340 = UNIT;
    }
    zgsz338 = true;
    goto finish_match_53;
  }
case_54: ;
  {
    if (zmergez3var.kind != Kind_zSTC) goto case_55;
    {
      uint64_t zgaz329;
      {
        uint64_t zgaz328;
        zgaz328 = zSFW_reg.zbits;
        {
          lbits zgsz3179;
          CREATE(lbits)(&zgsz3179);
          CONVERT_OF(lbits, fbits)(&zgsz3179, zgaz328, UINT64_C(8) , true);
          sail_int zgsz3180;
          CREATE(sail_int)(&zgsz3180);
          CONVERT_OF(sail_int, mach_int)(&zgsz3180, INT64_C(0));
          sail_int zgsz3181;
          CREATE(sail_int)(&zgsz3181);
          CONVERT_OF(sail_int, mach_int)(&zgsz3181, INT64_C(0));
          lbits zgsz3182;
          CREATE(lbits)(&zgsz3182);
          CONVERT_OF(lbits, fbits)(&zgsz3182, UINT64_C(0b1), UINT64_C(1) , true);
          lbits zgsz3183;
          CREATE(lbits)(&zgsz3183);
          vector_update_subrange_lbits(&zgsz3183, zgsz3179, zgsz3180, zgsz3181, zgsz3182);
          zgaz329 = CONVERT_OF(fbits, lbits)(zgsz3183, true);
          KILL(lbits)(&zgsz3183);
          KILL(lbits)(&zgsz3182);
          KILL(sail_int)(&zgsz3181);
          KILL(sail_int)(&zgsz3180);
          KILL(lbits)(&zgsz3179);
        }
      }
      struct zflag zgsz342;
      zgsz342 = zSFW_reg;
      zgsz342.zbits = zgaz329;
      zSFW_reg = zgsz342;
      unit zgsz343;
      zgsz343 = UNIT;
    }
    zgsz338 = true;
    goto finish_match_53;
  }
case_55: ;
  {
    if (zmergez3var.kind != Kind_zINR) goto case_56;
    uint64_t zr;
    zr = zmergez3var.zINR;
    uint64_t zv;
    zv = zread_reg8(zr);
    {
      uint64_t zgaz334;
      {
        uint64_t zgaz332;
        zgaz332 = zSFW_reg.zbits;
        uint64_t zgaz333;
        {
          bool zgaz331;
          {
            uint64_t zgaz330;
            {
              lbits zgsz3186;
              CREATE(lbits)(&zgsz3186);
              CONVERT_OF(lbits, fbits)(&zgsz3186, zv, UINT64_C(8) , true);
              sail_int zgsz3187;
              CREATE(sail_int)(&zgsz3187);
              CONVERT_OF(sail_int, mach_int)(&zgsz3187, INT64_C(3));
              sail_int zgsz3188;
              CREATE(sail_int)(&zgsz3188);
              CONVERT_OF(sail_int, mach_int)(&zgsz3188, INT64_C(0));
              lbits zgsz3189;
              CREATE(lbits)(&zgsz3189);
              vector_subrange_lbits(&zgsz3189, zgsz3186, zgsz3187, zgsz3188);
              zgaz330 = CONVERT_OF(fbits, lbits)(zgsz3189, true);
              KILL(lbits)(&zgsz3189);
              KILL(sail_int)(&zgsz3188);
              KILL(sail_int)(&zgsz3187);
              KILL(lbits)(&zgsz3186);
            }
            {
              lbits zgsz3184;
              CREATE(lbits)(&zgsz3184);
              CONVERT_OF(lbits, fbits)(&zgsz3184, zgaz330, UINT64_C(4) , true);
              lbits zgsz3185;
              CREATE(lbits)(&zgsz3185);
              CONVERT_OF(lbits, fbits)(&zgsz3185, UINT64_C(0xF), UINT64_C(4) , true);
              zgaz331 = eq_bits(zgsz3184, zgsz3185);
              KILL(lbits)(&zgsz3185);
              KILL(lbits)(&zgsz3184);
            }
          }
          if (zgaz331) {  zgaz333 = UINT64_C(0b1);  } else {  zgaz333 = UINT64_C(0b0);  }
        }
        {
          lbits zgsz3190;
          CREATE(lbits)(&zgsz3190);
          CONVERT_OF(lbits, fbits)(&zgsz3190, zgaz332, UINT64_C(8) , true);
          sail_int zgsz3191;
          CREATE(sail_int)(&zgsz3191);
          CONVERT_OF(sail_int, mach_int)(&zgsz3191, INT64_C(4));
          sail_int zgsz3192;
          CREATE(sail_int)(&zgsz3192);
          CONVERT_OF(sail_int, mach_int)(&zgsz3192, INT64_C(4));
          lbits zgsz3193;
          CREATE(lbits)(&zgsz3193);
          CONVERT_OF(lbits, fbits)(&zgsz3193, zgaz333, UINT64_C(1) , true);
          lbits zgsz3194;
          CREATE(lbits)(&zgsz3194);
          vector_update_subrange_lbits(&zgsz3194, zgsz3190, zgsz3191, zgsz3192, zgsz3193);
          zgaz334 = CONVERT_OF(fbits, lbits)(zgsz3194, true);
          KILL(lbits)(&zgsz3194);
          KILL(lbits)(&zgsz3193);
          KILL(sail_int)(&zgsz3192);
          KILL(sail_int)(&zgsz3191);
          KILL(lbits)(&zgsz3190);
        }
      }
      struct zflag zgsz345;
      zgsz345 = zSFW_reg;
      zgsz345.zbits = zgaz334;
      zSFW_reg = zgsz345;
      unit zgsz354;
      zgsz354 = UNIT;
    }
    {
      {
        lbits zgsz3195;
        CREATE(lbits)(&zgsz3195);
        CONVERT_OF(lbits, fbits)(&zgsz3195, zv, UINT64_C(8) , true);
        lbits zgsz3196;
        CREATE(lbits)(&zgsz3196);
        CONVERT_OF(lbits, fbits)(&zgsz3196, UINT64_C(0x01), UINT64_C(8) , true);
        lbits zgsz3197;
        CREATE(lbits)(&zgsz3197);
        add_bits(&zgsz3197, zgsz3195, zgsz3196);
        zv = CONVERT_OF(fbits, lbits)(zgsz3197, true);
        KILL(lbits)(&zgsz3197);
        KILL(lbits)(&zgsz3196);
        KILL(lbits)(&zgsz3195);
      }
      unit zgsz353;
      zgsz353 = UNIT;
    }
    {
      unit zgsz352;
      zgsz352 = zwrite_reg8(zr, zv);
    }
    {
      uint64_t zgaz338;
      {
        uint64_t zgaz336;
        zgaz336 = zSFW_reg.zbits;
        uint64_t zgaz337;
        {
          bool zgaz335;
          {
            lbits zgsz3198;
            CREATE(lbits)(&zgsz3198);
            CONVERT_OF(lbits, fbits)(&zgsz3198, zv, UINT64_C(8) , true);
            lbits zgsz3199;
            CREATE(lbits)(&zgsz3199);
            CONVERT_OF(lbits, fbits)(&zgsz3199, UINT64_C(0x00), UINT64_C(8) , true);
            zgaz335 = eq_bits(zgsz3198, zgsz3199);
            KILL(lbits)(&zgsz3199);
            KILL(lbits)(&zgsz3198);
          }
          if (zgaz335) {  zgaz337 = UINT64_C(0b1);  } else {  zgaz337 = UINT64_C(0b0);  }
        }
        {
          lbits zgsz3200;
          CREATE(lbits)(&zgsz3200);
          CONVERT_OF(lbits, fbits)(&zgsz3200, zgaz336, UINT64_C(8) , true);
          sail_int zgsz3201;
          CREATE(sail_int)(&zgsz3201);
          CONVERT_OF(sail_int, mach_int)(&zgsz3201, INT64_C(6));
          sail_int zgsz3202;
          CREATE(sail_int)(&zgsz3202);
          CONVERT_OF(sail_int, mach_int)(&zgsz3202, INT64_C(6));
          lbits zgsz3203;
          CREATE(lbits)(&zgsz3203);
          CONVERT_OF(lbits, fbits)(&zgsz3203, zgaz337, UINT64_C(1) , true);
          lbits zgsz3204;
          CREATE(lbits)(&zgsz3204);
          vector_update_subrange_lbits(&zgsz3204, zgsz3200, zgsz3201, zgsz3202, zgsz3203);
          zgaz338 = CONVERT_OF(fbits, lbits)(zgsz3204, true);
          KILL(lbits)(&zgsz3204);
          KILL(lbits)(&zgsz3203);
          KILL(sail_int)(&zgsz3202);
          KILL(sail_int)(&zgsz3201);
          KILL(lbits)(&zgsz3200);
        }
      }
      struct zflag zgsz346;
      zgsz346 = zSFW_reg;
      zgsz346.zbits = zgaz338;
      zSFW_reg = zgsz346;
      unit zgsz351;
      zgsz351 = UNIT;
    }
    {
      uint64_t zgaz342;
      {
        uint64_t zgaz340;
        zgaz340 = zSFW_reg.zbits;
        uint64_t zgaz341;
        {
          bool zgaz339;
          {
            lbits zgsz3205;
            CREATE(lbits)(&zgsz3205);
            CONVERT_OF(lbits, fbits)(&zgsz3205, zv, UINT64_C(8) , true);
            lbits zgsz3206;
            CREATE(lbits)(&zgsz3206);
            CONVERT_OF(lbits, fbits)(&zgsz3206, UINT64_C(0x7F), UINT64_C(8) , true);
            zgaz339 = eq_bits(zgsz3205, zgsz3206);
            KILL(lbits)(&zgsz3206);
            KILL(lbits)(&zgsz3205);
          }
          if (zgaz339) {  zgaz341 = UINT64_C(0b1);  } else {  zgaz341 = UINT64_C(0b0);  }
        }
        {
          lbits zgsz3207;
          CREATE(lbits)(&zgsz3207);
          CONVERT_OF(lbits, fbits)(&zgsz3207, zgaz340, UINT64_C(8) , true);
          sail_int zgsz3208;
          CREATE(sail_int)(&zgsz3208);
          CONVERT_OF(sail_int, mach_int)(&zgsz3208, INT64_C(7));
          sail_int zgsz3209;
          CREATE(sail_int)(&zgsz3209);
          CONVERT_OF(sail_int, mach_int)(&zgsz3209, INT64_C(7));
          lbits zgsz3210;
          CREATE(lbits)(&zgsz3210);
          CONVERT_OF(lbits, fbits)(&zgsz3210, zgaz341, UINT64_C(1) , true);
          lbits zgsz3211;
          CREATE(lbits)(&zgsz3211);
          vector_update_subrange_lbits(&zgsz3211, zgsz3207, zgsz3208, zgsz3209, zgsz3210);
          zgaz342 = CONVERT_OF(fbits, lbits)(zgsz3211, true);
          KILL(lbits)(&zgsz3211);
          KILL(lbits)(&zgsz3210);
          KILL(sail_int)(&zgsz3209);
          KILL(sail_int)(&zgsz3208);
          KILL(lbits)(&zgsz3207);
        }
      }
      struct zflag zgsz347;
      zgsz347 = zSFW_reg;
      zgsz347.zbits = zgaz342;
      zSFW_reg = zgsz347;
      unit zgsz350;
      zgsz350 = UNIT;
    }
    {
      uint64_t zgaz347;
      {
        uint64_t zgaz345;
        zgaz345 = zSFW_reg.zbits;
        uint64_t zgaz346;
        {
          bool zgaz344;
          {
            uint64_t zgaz343;
            zgaz343 = zxor_reduce(zv);
            {
              lbits zgsz3212;
              CREATE(lbits)(&zgsz3212);
              CONVERT_OF(lbits, fbits)(&zgsz3212, zgaz343, UINT64_C(1) , true);
              lbits zgsz3213;
              CREATE(lbits)(&zgsz3213);
              CONVERT_OF(lbits, fbits)(&zgsz3213, UINT64_C(0b0), UINT64_C(1) , true);
              zgaz344 = eq_bits(zgsz3212, zgsz3213);
              KILL(lbits)(&zgsz3213);
              KILL(lbits)(&zgsz3212);
            }
          }
          if (zgaz344) {  zgaz346 = UINT64_C(0b1);  } else {  zgaz346 = UINT64_C(0b0);  }
        }
        {
          lbits zgsz3214;
          CREATE(lbits)(&zgsz3214);
          CONVERT_OF(lbits, fbits)(&zgsz3214, zgaz345, UINT64_C(8) , true);
          sail_int zgsz3215;
          CREATE(sail_int)(&zgsz3215);
          CONVERT_OF(sail_int, mach_int)(&zgsz3215, INT64_C(2));
          sail_int zgsz3216;
          CREATE(sail_int)(&zgsz3216);
          CONVERT_OF(sail_int, mach_int)(&zgsz3216, INT64_C(2));
          lbits zgsz3217;
          CREATE(lbits)(&zgsz3217);
          CONVERT_OF(lbits, fbits)(&zgsz3217, zgaz346, UINT64_C(1) , true);
          lbits zgsz3218;
          CREATE(lbits)(&zgsz3218);
          vector_update_subrange_lbits(&zgsz3218, zgsz3214, zgsz3215, zgsz3216, zgsz3217);
          zgaz347 = CONVERT_OF(fbits, lbits)(zgsz3218, true);
          KILL(lbits)(&zgsz3218);
          KILL(lbits)(&zgsz3217);
          KILL(sail_int)(&zgsz3216);
          KILL(sail_int)(&zgsz3215);
          KILL(lbits)(&zgsz3214);
        }
      }
      struct zflag zgsz348;
      zgsz348 = zSFW_reg;
      zgsz348.zbits = zgaz347;
      zSFW_reg = zgsz348;
      unit zgsz349;
      zgsz349 = UNIT;
    }
    zgsz338 = true;
    goto finish_match_53;
  }
case_56: ;
  sail_match_failure("execute");
finish_match_53: ;
  zcbz310 = zgsz338;

end_function_57: ;
  return zcbz310;
end_block_exception_58: ;

  return false;
}

unit zmain(unit);

unit zmain(unit zgsz356)
{
  __label__ end_function_60, end_block_exception_61;

  unit zcbz311;
  {
    unit zgsz358;
    zgsz358 = zwrite_reg8(UINT64_C(0b000), UINT64_C(0x0F));
  }
  {
    uint64_t zgaz348;
    zgaz348 = z_get_flag_all(zSFW_reg);
    unit zgsz357;
    {
      lbits zgsz3219;
      CREATE(lbits)(&zgsz3219);
      CONVERT_OF(lbits, fbits)(&zgsz3219, zgaz348, UINT64_C(8) , true);
      zgsz357 = print_bits("flag reg before first cycle: ", zgsz3219);
      KILL(lbits)(&zgsz3219);
    }
  }
  bool zres;
  {
    struct zast zgaz354;
    CREATE(zast)(&zgaz354);
    zdecode8(&zgaz354, UINT64_C(0x04));
    zres = zexecute(zgaz354);
    KILL(zast)(&zgaz354);
  }
  {
    uint64_t zgaz349;
    zgaz349 = z_get_flag_all(zSFW_reg);
    unit zgsz359;
    {
      lbits zgsz3220;
      CREATE(lbits)(&zgsz3220);
      CONVERT_OF(lbits, fbits)(&zgsz3220, zgaz349, UINT64_C(8) , true);
      zgsz359 = print_bits("flag reg after first cycle: ", zgsz3220);
      KILL(lbits)(&zgsz3220);
    }
  }
  bool zresshadowz30;
  {
    struct zast zgaz353;
    CREATE(zast)(&zgaz353);
    zdecode8(&zgaz353, UINT64_C(0x04));
    zresshadowz30 = zexecute(zgaz353);
    KILL(zast)(&zgaz353);
  }
  {
    uint64_t zgaz350;
    zgaz350 = z_get_flag_all(zSFW_reg);
    unit zgsz360;
    {
      lbits zgsz3221;
      CREATE(lbits)(&zgsz3221);
      CONVERT_OF(lbits, fbits)(&zgsz3221, zgaz350, UINT64_C(8) , true);
      zgsz360 = print_bits("flag reg after second cycle: ", zgsz3221);
      KILL(lbits)(&zgsz3221);
    }
  }
  bool zresshadowz31;
  {
    struct zast zgaz352;
    CREATE(zast)(&zgaz352);
    zdecode8(&zgaz352, UINT64_C(0x04));
    zresshadowz31 = zexecute(zgaz352);
    KILL(zast)(&zgaz352);
  }
  uint64_t zgaz351;
  zgaz351 = z_get_flag_all(zSFW_reg);
  {
    lbits zgsz3222;
    CREATE(lbits)(&zgsz3222);
    CONVERT_OF(lbits, fbits)(&zgsz3222, zgaz351, UINT64_C(8) , true);
    zcbz311 = print_bits("flag reg after third cycle: ", zgsz3222);
    KILL(lbits)(&zgsz3222);
  }




end_function_60: ;
  return zcbz311;
end_block_exception_61: ;

  return UNIT;
}

unit zinitializze_registers(unit);

unit zinitializze_registers(unit zgsz361)
{
  __label__ end_function_63, end_block_exception_64;

  unit zcbz312;
  {
    {
      sail_int zgsz3223;
      CREATE(sail_int)(&zgsz3223);
      CONVERT_OF(sail_int, mach_int)(&zgsz3223, INT64_C(8));
      lbits zgsz3224;
      CREATE(lbits)(&zgsz3224);
      UNDEFINED(lbits)(&zgsz3224, zgsz3223);
      zA_reg = CONVERT_OF(fbits, lbits)(zgsz3224, true);
      KILL(lbits)(&zgsz3224);
      KILL(sail_int)(&zgsz3223);
    }
    unit zgsz366;
    zgsz366 = UNIT;
  }
  {
    zSFW_reg = zundefined_flag(UNIT);
    unit zgsz365;
    zgsz365 = UNIT;
  }
  {
    zBC_reg = zundefined_reg16(UNIT);
    unit zgsz364;
    zgsz364 = UNIT;
  }
  {
    zDE_reg = zundefined_reg16(UNIT);
    unit zgsz363;
    zgsz363 = UNIT;
  }
  {
    zHL_reg = zundefined_reg16(UNIT);
    unit zgsz362;
    zgsz362 = UNIT;
  }
  zSP_reg = zundefined_reg16(UNIT);
  zcbz312 = UNIT;
end_function_63: ;
  return zcbz312;
end_block_exception_64: ;

  return UNIT;
}

void model_init(void)
{
  setup_rts();
  current_exception = sail_new(struct zexception);
  CREATE(zexception)(current_exception);
  throw_location = sail_new(sail_string);
  CREATE(sail_string)(throw_location);
  zinitializze_registers(UNIT);
}

void model_fini(void)
{
  cleanup_rts();
  if (have_exception) {fprintf(stderr, "Exiting due to uncaught exception: %s\n", *throw_location);}
  KILL(zexception)(current_exception);
  sail_free(current_exception);
  KILL(sail_string)(throw_location);
  sail_free(throw_location);
  if (have_exception) {exit(EXIT_FAILURE);}
}

void model_pre_exit()
{
}

int model_main(int argc, char *argv[])
{
  model_init();
  if (process_arguments(argc, argv)) exit(EXIT_FAILURE);
  zmain(UNIT);
  model_fini();
  model_pre_exit();
  return EXIT_SUCCESS;
}

int main(int argc, char *argv[])
{
  return model_main(argc, argv);
}

#ifdef __cplusplus
}
#endif
