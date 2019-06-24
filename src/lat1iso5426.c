/*
 * Copyright (c) 1998, Wolfram Schneider <wosch@freebsd.org>
 *                     Konrad Zuse Zentrum f�r Informationstechnik Berlin.
 * All rights reserved.
 *
 * Read the file iso5426lat1.l for more information about iso5426.
 *
 */

/* Conversion of files between different charsets and usages.
   Copyright (C) 1990, 1993 Free Software Foundation, Inc.
   Francois Pinard <pinard@iro.umontreal.ca>, 1988.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
*/


#include "common.h"
#include "decsteps.h"

struct translation
  {
    int code;			/* code being translated */
    const char *string;		/* translation string */
  };

static struct translation diacritic_translations [] =
  {
#include "lat1iso5426.h"
    {0, NULL},
  };

static bool
init_latin1_iso5426 (RECODE_STEP step,
                     const struct recode_request *request,
                     RECODE_CONST_OPTION_LIST before_options _GL_UNUSED_PARAMETER,
                     RECODE_CONST_OPTION_LIST after_options _GL_UNUSED_PARAMETER)
{
  RECODE_OUTER outer = request->outer;

  char *pool;
  const char **table;
  unsigned counter;
  struct translation const *cursor;

  if (!ALLOC_SIZE (table, 256 * sizeof (char *) + 256, const char *))
    return false;
  pool = (char *) (table + 256);

  for (counter = 0; counter < 128; counter++)
    {
      pool[2 * counter] = counter;
      pool[2 * counter + 1] = '\0';
      table[counter] = pool + 2 * counter;
    }
  for (counter = 128; counter < 256; counter++)
    table[counter] = NULL;
  for (cursor = diacritic_translations; cursor->code; cursor++)
    table[cursor->code] = cursor->string;

  step->step_table = table;

  return true;
}

bool
module_latin1_iso5426 (RECODE_OUTER outer)
{
  return declare_single (outer, "Latin-1", "ISO_5426:1983-DB-MAB2", 
                         outer->quality_variable_to_byte, init_latin1_iso5426,
                         transform_byte_to_variable);
}

_GL_ATTRIBUTE_CONST void
delmodule_latin1_iso5426 (RECODE_OUTER outer _GL_UNUSED_PARAMETER)
{
}
