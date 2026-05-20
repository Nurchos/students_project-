import flet as ft

from db.database import init_db
from db.queries import (
    get_students,
    add_student,
    delete_student
)


def main(page: ft.Page):
    page.title = "Students App"

    column = ft.Column()

    name = ft.TextField(label="Name")
    age = ft.TextField(label="Age")
    course = ft.TextField(label="Course")

    def load_students(e=None):
        column.controls.clear()

        students = get_students()

        for s in students:
            sid = s[0]

            column.controls.append(
                ft.Row([
                    ft.Text(f"{s[1]} | {s[2]} | {s[3]}"),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=lambda e, sid=sid: remove_student(sid)
                    )
                ])
            )

        page.update()

    def add_new(e):
        add_student(
            name.value,
            int(age.value),
            course.value
        )

        load_students()

    def remove_student(student_id):
        delete_student(student_id)
        load_students()

    page.add(
        name,
        age,
        course,
        ft.ElevatedButton(
            "Add",
            on_click=add_new
        ),
        ft.ElevatedButton(
            "Load students",
            on_click=load_students
        ),
        column
    )


init_db()

ft.app(target=main)