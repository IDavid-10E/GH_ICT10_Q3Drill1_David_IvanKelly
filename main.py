from pyscript import document

def compute_average(event=None):

    score1 = int(document.getElementById("score1").value)
    score2 = int(document.getElementById("score2").value)

    average = (score1 + score2) // 2

    if average >= 75:
        result = "Yep"
    else:
        result = "Nah"

    document.getElementById("output").innerHTML = (
        "Average: " + str(average) + "<br>" +
        "Passed: " + result
    )
