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

#ifndef COMBOBOXDELEGATE_H_
#define CODEEDITOR_H_

#include <QItemDelegate>

/**
 *
 */
class ComboBoxDelegate: public QItemDelegate
{
  Q_OBJECT
    public:
    /**
     *
     * @param parent
     */
    ComboBoxDelegate(QObject *parent = 0);
    /**
     *
     * @param parent
     * @param option
     * @param index
     * @return
     */
    QWidget *
    createEditor(QWidget *parent, const QStyleOptionViewItem &option,
        const QModelIndex &index) const;
    /**
     *
     * @param editor
     * @param index
     */
    void
    setEditorData(QWidget *editor, const QModelIndex &index) const;
    /**
     *
     * @param editor
     * @param model
     * @param index
     */
    void
    setModelData(QWidget *editor, QAbstractItemModel *model,
        const QModelIndex &index) const;
    /**
     *
     * @param editor
     * @param option
     * @param index
     */
    void
    updateEditorGeometry(QWidget *editor,
        /**
         *
         */
        const QStyleOptionViewItem &option,
        const QModelIndex &index) const;
};

#endif  /* CODEEDITOR_H_ */
