from database import NoteManager

note_manager = NoteManager()


def main_menu():
    # Выбор действия
    print('''
Выберите действие:
1 - Добавить заметку
2 - Найти заметку
3 - Удалить заметку
''')
    action = input('Введите номер действия: ')
    if action == '1':
        add_note_input()
    elif action == '2':
        search()
    elif action == '3':
        delete()


def add_note_input():
    """Добавление заметки"""

    name = input('Введите название заметки: ')
    description = input('Введите описание заметки: ')
    note_manager.add_note(name, description)
    print('Заметка добавлена')
    main_menu()


def delete():
    """Удаление заметки"""
    all_notes = note_manager.get_all_notes()
    print("Список всех заметок:")
    for note in all_notes:
        print(f"ID: {note[0]}, Заголовок: {note[1]}")

    note_id_to_delete = input('Введите ID заметки которую хотите удалить: ')
    note_manager.delete_note(note_id_to_delete)
    print(f"\nЗаметка с ID {note_id_to_delete} удалена.")

    all_notes_after_deletion = note_manager.get_all_notes()
    print("\nСписок всех заметок после удаления:")
    for note in all_notes_after_deletion:
        print(f"ID: {note[0]}, Заголовок: {note[1]}")
    main_menu()


def search():
    all_notes = note_manager.get_all_notes()
    print("Список всех заметок:")
    if all_notes:
        for note in all_notes:
            print(f"ID: {note[0]}, Заголовок: {note[1]}")

        """Поиск заметок"""
        keyword = input(
            'Введите слово из описания по которому хотите найти заметку: ')
        search_result = note_manager.search_notes(keyword)
        print(f"\nРезультат поиска по ключевому слову '{keyword}':")
        if search_result:
            for note in search_result:
                print(f"ID: {note[0]} Заголовок: {note[1]}")

            """Просмотр подробной информации о заметке"""
            note_id_to_view = input(
                'Введите ID заметки, подробную информацию по которой вы хотите посмотреть: ')
            note_details = note_manager.get_note_details(note_id_to_view)
            print(f"\nПодробности о заметке с ID {note_id_to_view}:")
            print(f"Заголовок: {note_details[0]}")
            print(f"Содержание: {note_details[1]}")
    main_menu()


if __name__ == "__main__":
    main_menu()
