# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

# Входные данные
# В единственной строке входного файла INPUT.TXT записано единственное целое число N, 
# не превышающее по абсолютной величине 104.

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, 
# расположенных между 1 и N включительно.

def main():
    input_file = open("C:\PYTHON\Python_Summa\INPUT.TXT", "r")
    output_file = open("C:\PYTHON\Python_Summa\OUTPUT.TXT", "w")
    line = input_file.readline().split()
    x1 = int(line[0])
 
    summ = 0
    if x1 >=1:
        a = 1
        b = x1 + 1
 
    else:
        a = x1
        b = 2
 
    for i in range(a,b):
        summ = summ + i
 
        print(summ)
 
    print(summ)
 
 
    output_file.write(str(summ) + "\n")
 
    input_file.close()
    output_file.close()
 
 
if __name__ == "__main__":
    main()