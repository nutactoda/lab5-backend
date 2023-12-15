from app import app
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    matrix_size = 3
    operations_select = []
    matrix1_values = []
    matrix2_values = []
    multiply_matrix = []
    addition_matrix = []
    subtraction_matrix = []
    operations = ["Произведение", "Разность", "Сумма"]

    if request.method == "POST":
        if request.form['action'] == 'Показать':
            if request.values.get('matrix_size_input') != "":
                matrix_size = int(request.values.get('matrix_size_input'))

        if request.form['action'] == 'Очистить':
            if request.values.get('matrix_size_input') != "":
                matrix_size = int(request.values.get('matrix_size_input'))

        if request.form['action'] == 'Вычислить':
            matrix_size = int(request.values.get('matrix_size_input'))
            operation_id = request.values.getlist('operation[]')
            operations_select = [operations[int(i)] for i in operation_id]

            for i in range(matrix_size):
                row1 = []
                row2 = []
                for j in range(matrix_size):
                    if request.values.get(f"matrix1{i}{j}") != "":
                        matrix1_value = int(request.values.get(f"matrix1{i}{j}"))
                        row1.append(matrix1_value)
                    if request.values.get(f"matrix2{i}{j}") != "":
                        matrix2_value = int(request.values.get(f"matrix2{i}{j}"))
                        row2.append(matrix2_value)
                matrix1_values.append(row1)
                matrix2_values.append(row2)

            if "Произведение" in operations_select:
                n = matrix_size
                multiply_matrix = [[0] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            multiply_matrix[i][j] += matrix1_values[i][k] * matrix2_values[k][j]

            if "Разность" in operations_select:
                n = matrix_size
                subtraction_matrix = [[0 for j in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        subtraction_matrix[i][j] = matrix1_values[i][j] - matrix2_values[i][j]

            if "Сумма" in operations_select:
                n = matrix_size
                addition_matrix = [[0 for j in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        addition_matrix[i][j] = matrix1_values[i][j] + matrix2_values[i][j]


    html = render_template(
        'index.html',
        matrix_size=matrix_size,
        len=len,
        operations_select=operations_select,
        operation_list=operations,
        matrix1_values=matrix1_values,
        matrix2_values=matrix2_values,
        multiply_matrix=multiply_matrix,
        addition_matrix=addition_matrix,
        subtraction_matrix=subtraction_matrix
    )

    return html


app.run(debug=True)
