#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-gr", "--grade")
def add(filename, name, group, grade):
    """
    Добавить данные о студенте
    """
    # Запросить данные о студенте.
    students = load_students(filename)
    students.append(
        {
            'name': name,
            'group': group,
            'grade': grade,
        }
    )
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(students, fout, ensure_ascii=False, indent=4)
    click.secho("Студент добавлен", fg='green')


@cli.command()
@click.argument('filename')
def display(filename):
    """
    Вывести список студентов
    """
    # Заголовок таблицы.
    students = load_students(filename)
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


@cli.command()
@click.argument('filename')
def select(filename):
    """
    Отобразить студентов с баллом 4.0 и выше
    """
    students = load_students(filename)
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
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения студентов из списка.
    for student in students:
        grade = list(map(int, student.get('grade', '').split()))
        if sum(grade) / max(len(grade), 1) >= 4.0:
            count += 1
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    count,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('grade', 0)
                )
            )
    print(line)


def load_students(filename):
    """
    Загрузить список студентов из файла JSON
    """
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


if __name__ == '__main__':
    cli()
