
''' ROWS '''
# [print(f'Position for {i}: is row {i // 3}') for i in range(9)]

''' MODULOS FORMULA

a - (n * floor(a/n))

100 % 7 = 2
a = 100, n = 7
100 - (7 * floor(100/7)) = 2

'''

''' COLUMNS
If the numerator {i} is lower than the denominator {3}, 
the result will always be equal to the numerator.
'''
# [print(f'Position for {i}: is column {i % 3}') for i in range(12)]


pixels = [[1, 0, 1], [0, 0, 1], [1, 1, 0]]


def max_greyness():
    max_level = 0
    for cell in range(len(pixels)*len(pixels[0])):
        cell = cell - 1 if cell != 0 else cell
        length = len(pixels[0])

        # Step 1: sort the cell position according to the row and column
        cell_row_index = cell // length
        cell_col_index = cell % length

        # Step 2: Extract the numbers before, after, up and down the selected cell.
        row_area = list()
        col_area = list()

        for index, value in enumerate(pixels):
            if index == cell_row_index:
                row_area.extend(value)

        for row in pixels:
            for index, value in enumerate(row):
                if index == cell_col_index:
                    col_area.append(value)

        # Step 3: Sum up the 1's and 0's and apply the formula for levels of grayness
        # g = (1's + 1's) - (0's + 0's)

        grey_level = (sum(row_area) + sum(col_area)) - \
            ((length - sum(row_area))+(length - sum(col_area)))

        # Step 5: Print the max greyness level
        max_level = grey_level if grey_level > max_level else max_level

    return max_level


if __name__ == '__main__':

    print(max_greyness())
