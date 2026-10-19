
from pyscript import document

grade_7 = {"Brooke Bagiuo", "grade 7 student 1", "grade 7 student 2"}
grade_8 = {"grade 8 student 1", "grade 8 student 2", "grade student 3"}
grade_9 = {"Sky Bagiuo", "grade 9 student 2", "grade 9 student 3"}
grade_10 = {"Sophia Tan", "Bela Allas", "Joaquin Tabije", "Macy Panela", "Daphne Mariano", "Pocholo Comanda", "Juan Miguel Piansay", "Mohammad Calaca"}

def main(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    new_member_set = {f"{first_name} {last_name}"}

    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member_set

    members_html = "</li>\n    <li>".join(master_set)

    output_content = f"""
    club summary<br>
    Total Number of Members: {len(master_set)}<br><br>
    Full List of All Members:
    <ul>
        <li>{members_html}</li>
    </ul>
    """

    document.getElementById("output").innerHTML = output_content