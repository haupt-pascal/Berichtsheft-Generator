from docxtpl import DocxTemplate
import random
from datetime import date
from calendarweek import CalendarWeek

doc = DocxTemplate('Vorlage_Neu.docx')

randomList = {
    'Audio-Logs überprüfen',
    'Logger-Scripte überprüfen',
    'Virtuelle Maschinen erstellen und einrichten',
    'Ticketsystem pflegen',
    'Mitschnitt-Server prüfen',
    'Laptops einrichten',
    'AD-Richtlinien anpassen',
    'Sicherheitslücken prüfen und beheben',
    'Computer einrichten',
    'Projektplanung',
    'Patching von virtuellen Maschinen',
    'Switche konfigurieren und einbauen',
    'Skripte zur Automatisierung aktualisieren',
    '',
    '',
    ''
}

nr_input = input("Ausbildungsnachweis-Nummer (-1 rechnen & angeben): ")
nr = int(nr_input) - 1
my_start_date = input("Start-Tag (Bsp. 01: ")
my_start_month = input("Start-Monat (Bsp. 12): ")
my_start_year = input("Start-Jahr (Bsp. 2022): ")
my_end_date = input("End-Tag (Bsp. 01): ")
my_end_month = input("End-Monat (Bsp. 12): ")
my_end_year = input("End-Jahr (Bsp. 2022): ")
start = date(int(my_start_year), int(my_start_month), int(my_start_date))
end = date(int(my_end_year), int(my_end_month), int(my_end_date))
weeks = CalendarWeek.weeks_within(start, end)

for week in weeks:
    random_pick = random.sample(randomList, 7)

    input1 = [0]
    input2 = [1]
    input3 = [2]
    input4 = [3]
    input5 = [4]
    input6 = [5]
    input7 = [6]

    res_input1 = [random_pick[i] for i in input1]
    res_input2 = [random_pick[i] for i in input2]
    res_input3 = [random_pick[i] for i in input3]
    res_input4 = [random_pick[i] for i in input4]
    res_input5 = [random_pick[i] for i in input5]
    res_input6 = [random_pick[i] for i in input6]
    res_input7 = [random_pick[i] for i in input7]

    line1 = '[%s]' % ', '.join(map(str, res_input1))
    line2 = '[%s]' % ', '.join(map(str, res_input2))
    line3 = '[%s]' % ', '.join(map(str, res_input3))
    line4 = '[%s]' % ', '.join(map(str, res_input4))
    line5 = '[%s]' % ', '.join(map(str, res_input5))
    line6 = '[%s]' % ', '.join(map(str, res_input6))
    line7 = '[%s]' % ', '.join(map(str, res_input7))

    res1 = str(line1)[1:-1]
    res2 = str(line2)[1:-1]
    res3 = str(line3)[1:-1]
    res4 = str(line4)[1:-1]
    res5 = str(line5)[1:-1]
    res6 = str(line6)[1:-1]
    res7 = str(line7)[1:-1]

    start_day = week[1]
    end_day = week[6]
    start_day_string = start_day.strftime("%d.%m.%Y")
    end_day_string = end_day.strftime("%d.%m.%Y")
    nr = int(nr) + 1

    month = str(week)[14:-18]
    year = str(week)[9:-21]

    context = {
        'week_input1': res1,
        'week_input2': res2,
        'week_input3': res3,
        'week_input4': res4,
        'week_input5': res5,
        'week_input6': res6,
        'week_input7': res7,
        'nr': nr,
        'month': month,
        'year': year,
        'start_date':start_day_string,
        'end_date': end_day_string
    }
    print(context)
    doc.render(context)
    doc.save(str(nr)+".docx")