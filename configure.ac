# Configure template for Recode.
# Copyright (C) 1994-2018 Free Software Foundation, Inc.
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.69)
AC_INIT(recode, 3.7, [rrt@sc3d.org])
AC_CONFIG_SRCDIR(src/recode.c)
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE
AC_CONFIG_MACRO_DIR(m4)
AC_CANONICAL_HOST

AC_PROG_CC_C99
gl_EARLY
LT_INIT
AC_PROG_LEX
AX_PYTHON_PATH
AX_PYTHON_VERSION_ENSURE([2.2])
gl_INIT

dnl help2man
dnl Set a value even if not found, so that an invocation via build-aux/missing works
AX_WITH_PROG([HELP2MAN], [help2man], [help2man])

AC_SUBST([objdir])
LT_SYS_MODULE_EXT
AC_SUBST([shlibext], [$libltdl_cv_shlibext])

dnl Extra warnings with GCC and compatible compilers
AC_ARG_ENABLE([gcc-warnings],
  [AS_HELP_STRING([--disable-gcc-warnings],
                  [turn off lots of GCC warnings])],
  [case $enableval in
     yes|no) ;;
     *)      AC_MSG_ERROR([bad value $enableval for gcc-warnings option]) ;;
   esac
   gl_gcc_warnings=$enableval],
  [gl_gcc_warnings=yes]
)
if test "$gl_gcc_warnings" = yes; then
  dnl Set up the list of undesired warnings.
  nw=
  nw="$nw -Wsystem-headers"   # Don’t let system headers trigger warnings
  nw="$nw -Wundef"            # All compiler preprocessors support #if UNDEF
  nw="$nw -Wtraditional"      # All compilers nowadays support ANSI C
  nw="$nw -Wdeclaration-after-statement" # We require C99.
  nw="$nw -Wstrict-overflow"  # Use a lower level (see below).
  nw="$nw -Wconversion"       # These warnings usually don’t point to mistakes.
  nw="$nw -Wsign-conversion"  # Likewise.

  gl_MANYWARN_ALL_GCC([warnings])

  dnl Enable all GCC warnings not in this list.
  gl_MANYWARN_COMPLEMENT([warnings], [$warnings], [$nw])
  for w in $warnings; do
    gl_WARN_ADD([$w])
  done

  dnl Add an extra warning
  gl_WARN_ADD([-Wstrict-overflow=1])
  dnl Add some more safety measures
  gl_WARN_ADD([-D_FORTIFY_SOURCE=2])
  dnl Remove a warning being promoted to error: we trigger this and can't turn it off with pragmas.
  gl_WARN_ADD([-Wno-error=format-security])

  # When compiling with GCC, prefer -isystem to -I when including system
  # include files, to avoid generating useless diagnostics for the files.
  ISYSTEM='-isystem '
else
  ISYSTEM='-I'
fi
AC_SUBST([ISYSTEM])

AC_CONFIG_HEADERS([config.h])
AC_HEADER_STDC
AM_ICONV
LIBS="$LIBICONV $LIBS"
AM_WITH_DMALLOC

AM_GNU_GETTEXT_VERSION(0.19)
AM_GNU_GETTEXT(external)

AC_OUTPUT(Makefile contrib/Makefile doc/Makefile lib/Makefile
          po/Makefile.in src/Makefile tests/Makefile tests/setup.py)
