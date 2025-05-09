#!/usr/bin/env python3
import os
import subprocess

def run_all():
    print("Pokrećem sve testove iz poc_scripts...")
    scripts = [f for f in os.listdir("poc_scripts") if f.endswith(".py")]
    for script in scripts:
        print(f"[*] Pokrećem: {script}")
        subprocess.run(["python3", f"poc_scripts/{script}"])
        print("-" * 50)

def run_selected():
    print("Dostupni testovi:")
    scripts = [f for f in os.listdir("poc_scripts") if f.endswith(".py")]
    for i, script in enumerate(scripts):
        print(f"[{i+1}] {script}")
    choices = input("Unesi brojeve testova odvojenih zarezom (npr. 1,3,5): ")
    indices = [int(i.strip()) - 1 for i in choices.split(",")]
    for idx in indices:
        script = scripts[idx]
        print(f"[*] Pokrećem: {script}")
        subprocess.run(["python3", f"poc_scripts/{script}"])
        print("-" * 50)

def view_results():
    print("Rezultati u folderu 'results/':")
    os.system("ls -lh results")

def generate_report():
    print("Generišem izveštaj...")
    os.system("python3 logics/generate_report.py")

def edit_targets():
    os.system("nano targets/targets.txt")

def ai_analyze():
    print("Pokrećem AI analizu rezultata...")
    os.system("python3 ai_analyze_results.py")

while True:
    os.system("clear")
    print("""BugHunt Terminal Menu

[1] Pokreni sve testove (FULL scan)
[2] Pokreni odabrane testove
[3] Pregled rezultata (results/)
[4] Generiši izveštaj (Markdown / JSON / CSV)
[5] Podesi metu (targets.txt)
[6] Izlaz
[7] AI analiza rezultata (.txt > .md)
""")
    choice = input("Unesi opciju: ").strip()
    
    if choice == "1":
        run_all()
    elif choice == "2":
        run_selected()
    elif choice == "3":
        view_results()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        edit_targets()
    elif choice == "6":
        print("Izlaz...")
        break
    elif choice == "7":
        ai_analyze()
    else:
        print("Nepoznata opcija!")
    

    input("\nPritisni Enter za nastavak...")
BugHunt Terminal Menu

[1] Pokreni sve testove (FULL scan)
[2] Pokreni odabrane testove
[3] Pregled rezultata (results/)
[4] Generiši izveštaj (Markdown / JSON / CSV)
[5] Podesi metu (targets.txt)
[6] Izlaz

Unesi opciju: 
""")
    choice = input().strip()
    
    if choice == "1":
        run_all()
    elif choice == "2":
        run_selected()
    elif choice == "3":
        view_results()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        edit_targets()
    elif choice == "6":
        print("Izlaz...")
        break
    else:
        print("Nepoznata opcija!")
    
    input("\nPritisni Enter za nastavak...")

