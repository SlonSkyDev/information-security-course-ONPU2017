import argparse

parcer = argparse.ArgumentParser()

parcer.add_argument('mode', help='Encript or Decript',
                    choices=['enc', 'dec'])
parcer.add_argument('inputPath', help='Path to input file')
parcer.add_argument('outputPath', help='Path to output file ' +
                                       '(will be created new one)')
parcer.add_argument('keyPath', help='Path to key file')
parcer.add_argument('-ka', '--keys-creation-algorithm',
                    default='round', choices=['round', 'scrambler'],
                    help='"round" - для i-го раунда подключом Vi является ' +
                         'цепочка из 32-х подряд идущих бит за-данного ключа' +
                         ', которая начинается с бита номер i, продолжается ' +
                         'до последнего бита ключа и при его достижении ' +
                         'циклически повторяется, начиная с 1 бита;' +
                         '"scrambler" - для i-го раунда, начиная с бита ' +
                         'номер i, берется цепочка из 8-ми подряд идущих ' +
                         'битов ключа, которая является начальным значением ' +
                         'для скремблера вида 0000 00112; подключом Vi ' +
                         'является сгенерированная этим скремблером ' +
                         'последовательность из 32-х бит;')
parcer.add_argument('-fa', '--cription-function-algorithm',
                    default='identical', choices=['identical', 'xor'],
                    help='"identical" - функция F – единичная, т.е. ' +
                         'F(Vi)=Vi; "xor" - функция имеет вид ' +
                         'F(Vi, X)=S(X)xorVi, где S(X) – левая часть ' +
                         'шифруемого блока, на которую посредством операции ' +
                         'XOR была наложена 32-х битная последовательность, ' +
                         'сгенерированная 16-ти разрядным скремблером вида ' +
                         '0100 0000 0000 00112;')

def encriptionFunction(block, key):
    pass

def decriptionFunction(block, key):
    pass

def round(left, right):
    pass

def encript(message, keys):
    pass

def decript(message, keys):
    pass