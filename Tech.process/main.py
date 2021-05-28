from dataclasses import dataclass, field
from typing import List

result = []


@dataclass
class OperationNotes:
    operation: str
    operationDesc: List = field(default_factory=list)


@dataclass
class Operation:
    name: str
    desc: List = field(default_factory=list)


def Notes(array: list) -> None:
    print('Примечание:', end=' ')
    answer = input()
    array.append(OperationNotes(operation=answer))


def VariablesPrint(text: str) -> None:
    print(text)
    print('Ответ:', end=' ')


def Output(name: str, notes: list) -> None:
    if len(name) != 0:
        result.append(Operation(name=name, desc=notes))


def Turning() -> None:
    name: str = ''
    notes = []
    while True:
        print('1. Токарная с припуском. 2. Токарная в р-р. 3. Примечания. 4. Выход.')
        print('Ответ:', end=' ')
        answer = input()
        if answer == '1':
            name = 'Токарная с припуском'
        elif answer == '2':
            name = 'Токарная в р-р'
        elif answer == '3':
            Notes(notes)
        else:
            Output(name, notes)
            break


def Boring() -> None:
    name: str = ''
    notes = []

    def NotesForBoring(notes_boring: list) -> None:

        def WireHoles(array: list):
            while True:
                VariablesPrint(
                    '1. Круглое отверстие. 2. Некруглое отверстие. 3. Выход')
                answer = input()
                if answer == '1':
                    print('Кол-во отверстий:', end=' ')
                    quanityHoles = input()
                    print('Исходный диаметр отверстий:', end=' ')
                    originalDiameter = input()
                    print('Диаметр отверстий под проволоку:', end=' ')
                    wireDiameter = input()
                    resultWireHoles = '%s отв. ф%s -> ф%s' % (
                        quanityHoles, originalDiameter, wireDiameter)
                    array.append(resultWireHoles)
                elif answer == '2':
                    print('Диаметр отверстий под пройму:', end=' ')
                    wireDiameter = input()
                    resultWireHoles = 'в пройме ф%s' % (wireDiameter)
                    array.append(resultWireHoles)
                else:
                    break

        while True:
            VariablesPrint(
                '1. Отверстия под проволоку. 2. Остальные отверстия в р-р. 3. Резать резьбу. 4. Выход.')
            answer = input()
            if answer == '1':
                notes_wire_holes = []
                WireHoles(notes_wire_holes)
                notes_boring.append(OperationNotes(
                    operation='под проволоку:', operationDesc=notes_wire_holes))
            elif answer == '2':
                notes_boring.append(OperationNotes(
                    operation='остальные в р-р'))
            elif answer == '3':
                notes_boring.append(OperationNotes(operation='резать резьбу'))
            else:
                break

    while True:
        VariablesPrint(
            '1. Расточка с примечаниями. 2. Расточка в р-р. 3. Примечания. 4. Выход.')
        answer = input()
        if answer == '1':
            name = 'Расточка:'
            NotesForBoring(notes)
        elif answer == '2':
            name = 'Расточка в р-р.'
        elif answer == '3':
            Notes(notes)
        else:
            Output(name, notes)
            break


result.append(Operation(name='Заготовка'))

while True:
    VariablesPrint('Выберите операцию:\n1. Токарная. 2. Расточка 3. Выход')
    answer = input()
    if answer == '1':
        Turning()
    elif answer == '2':
        Boring()
    else:
        break

    print('')
    for i in range(len(result)):
        print('%i. %s' % (i+1, result[i].name))
        if len(result[i].desc) != 0:
            for j in range(len(result[i].desc)):
                if len(result[i].desc[j].operationDesc) != 0:
                    print(result[i].desc[j].operation)
                    for k in range(len(result[i].desc[j].operationDesc)):
                        print(result[i].desc[j].operationDesc[k], end=";\n")
                else:
                    print(result[i].desc[j].operation, end=";\n")
    print('')
