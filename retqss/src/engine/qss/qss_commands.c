/*****************************************************************************

 This file is part of QSS Solver.

 QSS Solver is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 QSS Solver is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with QSS Solver.  If not, see <http://www.gnu.org/licenses/>.

 ******************************************************************************/

#include "qss/qss_commands.h"

#include <stdlib.h>

#include "../common/data.h"
#include "../common/utils.h"
#include "qss_data.h"
#include "qss_scheduler.h"
#include "qss_simulator.h"

QSS_simulator **_simulator = NULL;


void
QSS_terminate(SC_scheduler scheduler, QSS_data simData, QSS_time simTime)
{
  simData->ft = simTime->time;
  simTime->time = INF;
}

void
QSS_CMD_alloc(QSS_simulator simulator)
{
  // TODO - retQSS
  _simulator = checkedMalloc(sizeof(QSS_simulator*));
  *_simulator = checkedMalloc(sizeof(QSS_simulator));
  (*_simulator)[0] = simulator;
}

void
QSS_CMD_realloc(QSS_simulator simulator)
{
  // TODO - retQSS
  int lps = simulator->data->params->lps;
  if(lps > 0)
	  *_simulator = realloc(*_simulator, (lps+1) * sizeof(QSS_simulator));
}

void
QSS_CMD_terminate()
{
  int i, lps = (*_simulator)[0]->data->params->lps;
  if(lps == 0)
  {
    lps = 1;
  }
  // TODO - retQSS
  for(i = 1; i <= lps; i++)
  {
    SC_setUpdate((*_simulator)[i]->scheduler, QSS_terminate);
  }
}

void
QSS_CMD_init(QSS_simulator simulator)
{
  // TODO - retQSS
  (*_simulator)[simulator->id+1] = simulator;
}

void
QSS_CMD_free()
{
  if(*_simulator != NULL)
  {
    free(*_simulator);
  }
  free(_simulator);
}

