import argparse, os

def file_data(filepath):
    if os.path.exists(filepath)==False:
        print("Error! Archivo no encontrado.")
        return
    with open(filepath, 'r') as file:
        return file.readlines()

def validatedata(data):
    try:
        numbers_list = []
        for num in data:
            numbers_list.append(float( num ))
        return numbers_list
    except:
        print("Error! No es un numero.")
        return

def operacion(nums):
    result = 0
    for n in nums:
        if n != None:
            result += n
    return result

def printresult(nums, result):
  print(' + '.join([str(i) for i in nums if i != None])+' = '+str(result))

def sum_numbers(filepath):
  filedata = file_data( filepath )
  nums = validatedata( filedata)
  result=operacion(nums)
  printresult(nums, result)

if __name__=="__main__":
  ap=argparse.ArgumentParser()
  ap.add_argument('-inputfile', dest='inputfile', required=True, help='path to input file')
  args=ap.parse_args()
  sum_numbers(args.inputfile)
