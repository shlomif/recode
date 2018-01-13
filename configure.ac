# Configure template for Recode.
# Copyright (C) 1994-2018 Free Software Foundation, Inc.
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.69)
AC_INIT(recode, 3.7-beta2, [rrt@sc3d.org])
AC_CONFIG_SRCDIR(src/recode.c)
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE
AC_CONFIG_MACRO_DIR(m4)
AC_CANONICAL_HOST

AC_PROG_CC_C99
gl_EARLY
LT_INIT
AC_PROG_LEX
gl_INIT

AC_CONFIG_HEADERS([config.h])
AC_HEADER_STDC
AM_ICONV
LIBS="$LIBICONV $LIBS"
AM_WITH_DMALLOC

AM_GNU_GETTEXT_VERSION(0.18)
AM_GNU_GETTEXT(external)

AM_CONDITIONAL(MES_SITES, [test -f "~/etc/mes-sites/site.mk"])

AH_BOTTOM([
#include "cleaner.h"
])

AC_OUTPUT(Makefile cleaner.h contrib/Makefile doc/Makefile lib/Makefile
          po/Makefile.in src/Makefile tests/Makefile tests/setup.py)
