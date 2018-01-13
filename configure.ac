# Configure template for Recode.
# Copyright (C) 1994-2018 Free Software Foundation, Inc.
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.69)
AC_INIT(recode, 3.7-beta2, [rrt@sc3d.org])
AC_CONFIG_SRCDIR(src/recode.c)
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE
AC_CONFIG_MACRO_DIR(m4)

AC_PROG_CC
gl_EARLY
LT_INIT
AC_FUNC_ALLOCA
AC_ISC_POSIX
AC_C_CONST
AC_C_INLINE
AC_PROG_LEX
gl_INIT

AC_CONFIG_HEADERS([config.h])
AC_HEADER_STDC
AC_CHECK_HEADERS(limits.h locale.h memory.h stdbool.h stddef.h stdlib.h string.h unistd.h utime.h)
AC_TYPE_SIGNAL
jm_STRUCT_UTIMBUF

AM_ICONV
LIBS="$LIBICONV $LIBS"

AC_CHECK_FUNCS(dup2 mbrtowc rename setlocale strerror strndup wcrtomb)
AC_REPLACE_FUNCS(strtol strtoul)
AC_FUNC_ALLOCA
AC_FUNC_VPRINTF

jm_FUNC_MALLOC
jm_FUNC_REALLOC

AC_CANONICAL_HOST
jm_LANGINFO_CODESET
jm_GLIBC21

AM_WITH_DMALLOC

AM_GNU_GETTEXT_VERSION(0.18)
AM_GNU_GETTEXT(external)

AM_CONDITIONAL(MES_SITES, [test -f "~/etc/mes-sites/site.mk"])

AH_BOTTOM([
#include "cleaner.h"
])

AC_OUTPUT(Makefile cleaner.h contrib/Makefile doc/Makefile lib/Makefile
          po/Makefile.in src/Makefile tests/Makefile tests/setup.py)
