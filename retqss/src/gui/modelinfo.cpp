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

#include <QFileInfo>

#include "modelinfo.h"

ModelInfo::ModelInfo(QString fullname)
{
  setFullname(fullname);
  _dirty = false;
  if(name().endsWith(".log"))
  {
    _init = false;
  }
  else
  {
    _init = true;
  }
}

ModelInfo::~ModelInfo()
{
  return;
}

QString
ModelInfo::baseName()
{
  QFileInfo fi(_fullname);
  return fi.baseName();
}

QString
ModelInfo::name()
{
  QFileInfo fi(_fullname);
  return fi.fileName();
}

QString
ModelInfo::path()
{
  QFileInfo fi(_fullname);
  return fi.absolutePath();
}
