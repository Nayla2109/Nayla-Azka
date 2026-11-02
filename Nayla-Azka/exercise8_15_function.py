# Exercise 8-15: Printing Models
def printModels(unprintedDesigns, completedModels):
    # Mensimulasikan pencetakan desain hingga tidak ada lagi yang tersisa.
    # Memindahkan setiap desain ke completed_models setelah dicetak.
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop(0)
        print(f"Mencetak model: {currentDesign}")
        completedModels.append(currentDesign)

def showCompletedModels(completedModels):
    # Menampilkan semua model yang telah dicetak.
    print("\nModel berikut telah dicetak:")
    for completedModel in completedModels:
        print(f"- {completedModel}")