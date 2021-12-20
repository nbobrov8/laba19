#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click


def add_student(students, name, group, grade, file_name):
    # Запросить данные о студенте.
    students.append(
        {
            'name': name,
            'group': group,
            'grade': grade,
        }
    )
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(students, fout, ensure_ascii=False, indent=4)
    return students


def show_list(students):
    # Заголовок таблицы.
    if students:

        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"
            )
        )
        print(line)

        # Вывести данные о всех студентах.
        for idx, student in enumerate(students, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('grade', 0)
                )
            )
        print(line)
    else:
        print("Список студентов пуст.")


def show_selected(students):
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения студентов из списка.
    for student in students:
        grade = list(map(int, student.get('grade', '').split()))
        if sum(grade) / max(len(grade), 1) >= 4.0:
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №', student.get('group', ''))
            )
            count += 1
    if count == 0:
        print("Студенты с баллом 4.0 и выше не найдены.")


def load_students(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


@click.command()
@click.option("-c", "--command")
@click.argument('filename')
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-gr", "--grade")
@click.option("-s", "--select")
def main(command, filename, students, name, group, grade):
    if command == 'add':
        add_student(students, name, group, grade, filename)
        click.secho('Студент добавлен', fg='green')
    elif command == 'display':
        show_list(students)
    elif command == 'select':
        show_selected(students)


if __name__ == '__main__':
    main()
