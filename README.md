# python-algorithms

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Реализация алгоритмов и структур данных на Python

## Installation

```bash
pip install -r requirements.txt
```

или

```bash
uv sync
```

## Algorithms

### Sorts

- [Bubble Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/bubble_sort.py)

Перебираются все элементы массива по одному и сравниваются с предыдущим элементом.
Если элемент слева больше чем справа, то он перемещается в позицию справа.

- [bucket Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/bucket_sort.py)

Массив разбивается на бакеты, после каждый элемент закидывается в соответствующий бакет.
Далее это рекурсивно повторяктся для каждого бакета, пока в одном бакете не будет один или менее элементов.

- [Counting Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/counting_sort.py)

Вычисляется диапозон всех чисел и создается массив длины диапозона.
Далее перебираются каждый элемент закидывается в соответствующий индекс нового массива.
После этого из нового массива по возрастанию в исходный массив добавляются элементы ровно в том количестве раз какое они были перемещены.

- [Heap Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/heap_sort.py)

Похоже на сортировку выбором, но за основу взята структура данных куча, которая позволяет брать минимум за логарифм.

- [Quick Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/quick_sort.py)

Выбирается опорный элемент, строятся 2 массива, где в одном все элементы больше, а в другом меньше опорного.
Далее эти 2 массива рекурсивно сортируются и соединяются в один массив вместе с опорным элементом.

- [Radix Sort](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/sorts/radix_sort.py)

LSD: Сортируются от меньшего разряда к большему. После каждой итерации ранее отсортированные значения в элементах сохраняют порядок.

### Factorial

- [iteration](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/factorial/iteration.py)

Хранится значения предыдущих факториалов в массиве, после каждой итерации добавляется новое значение и сохраняется порядок.

- [recursive](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/factorial/recursive.py)

Рекурсивно вычисляется факториал для заданного числа, от наибольшего к наименьшему.

### Fibonacci

- [iteration](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/fibonacci/iteration.py)

Хранятся предыдущие значения и перезаписываются после их суммирования.

- [matrix power](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/fibonacci/matrix_power.py)

Строится матрица, которая является степенью факториала для заданного числа.
Далее она бинарно возводится в степень, что позволяет получить значение факториала за логарифм без потери точности.

- [recursive](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/algorithms/fibonacci/recursive.py)

Рекурсивно вычисляется факториал для заданного числа, от наибольшего к наименьшему.

## Structures

### Queue

- [base](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/queue/base.py)

Интерфейс для очередей.

- [queue dynamic array](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/queue/queue_dynamic_array.py)

Реализация очереди на динамическом массиве.

- [queue linked list](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/queue/queue_linked_list.py)

Реализация очереди на связанном списке.

- [queue with stack](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/queue/queue_with_stack.py)

Реализация очереди на двух стеках.

### Stack

- [base](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/stack/base.py)

Интерфейс для стеков.

- [stack dynamic array](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/stack/stack_dynamic_array.py)

Реализация стека на динамическом массиве.

- [stack linked list](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/stack/stack_linked_list.py)

Реализация стека на связанном списке.

- [stack with queue](https://github.com/hesoyamTM/python-algorithms/blob/main/src/usecase/structs/stack/stack_with_queue.py)

Реализация стека на очереди.
