from pyscript import Element

class SortableTable:
    def __init__(self, table_node):
        self.table_node = table_node
        self.column_headers = table_node.querySelectorAll('thead th')
        self.sort_columns = []
        
        for i, ch in enumerate(self.column_headers):
            button_node = ch.querySelector('button')
            if button_node:
                self.sort_columns.append(i)
                button_node.setAttribute('data-column-index', str(i))
                button_node.addEventListener('click', self.handle_click)
        
        self.option_checkbox = Element('show-unsorted')
        if self.option_checkbox:
            self.option_checkbox.element.addEventListener('change', self.handle_option_change)
            if self.option_checkbox.element.checked:
                self.table_node.classList.add('show-unsorted-icon')
        
    def set_column_header_sort(self, column_index):
        if isinstance(column_index, str):
            column_index = int(column_index)

        for i, ch in enumerate(self.column_headers):
            button_node = ch.querySelector('button')
            if i == column_index:
                value = ch.getAttribute('aria-sort')
                if value == 'descending':
                    ch.setAttribute('aria-sort', 'ascending')
                    self.sort_column(column_index, 'ascending', 'num' in ch.classList)
                else:
                    ch.setAttribute('aria-sort', 'descending')
                    self.sort_column(column_index, 'descending', 'num' in ch.classList)
            else:
                if ch.hasAttribute('aria-sort') and button_node:
                    ch.removeAttribute('aria-sort')

    def sort_column(self, column_index, sort_value, is_number):
        def compare_values(a, b):
            if sort_value == 'ascending':
                if a['value'] == b['value']:
                    return 0
                elif is_number:
                    return a['value'] - b['value']
                else:
                    return -1 if a['value'] < b['value'] else 1
            else:
                if a['value'] == b['value']:
                    return 0
                elif is_number:
                    return b['value'] - a['value']
                else:
                    return -1 if a['value'] > b['value'] else 1
        
        tbody_node = self.table_node.querySelector('tbody')
        row_nodes = []
        data_cells = []

        row_node = tbody_node.firstElementChild
        index = 0
        while row_node:
            row_nodes.append(row_node)
            row_cells = row_node.querySelectorAll('th, td')
            data_cell = row_cells[column_index]
            data = {'index': index, 'value': data_cell.textContent.lower().strip()}
            if is_number:
                data['value'] = float(data['value'])
            data_cells.append(data)
            row_node = row_node.nextElementSibling
            index += 1

        data_cells.sort(compare_values)

        while tbody_node.firstChild:
            tbody_node.removeChild(tbody_node.lastChild)

        for i in range(len(data_cells)):
            tbody_node.appendChild(row_nodes[data_cells[i]['index']])

    def handle_click(self, event):
        tgt = event.currentTarget
        self.set_column_header_sort(int(tgt.getAttribute('data-column-index')))
    
    def handle_option_change(self, event):
        tgt = event.currentTarget
        if tgt.checked:
            self.table_node.classList.add('show-unsorted-icon')
        else:
            self.table_node.classList.remove('show-unsorted-icon')

# Initialize sortable table buttons
def initialize_sortable_tables():
    sortable_tables = document.querySelectorAll('table.sortable')
    for table in sortable_tables:
        SortableTable(table)

initialize_sortable_tables()