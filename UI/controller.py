import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdowns(self):
        opzioni_bib = [ft.dropdown.Option(key="Tutte", text="Tutte")]
        for b in self._model.get_biblioteche():
            opzioni_bib.append(ft.dropdown.Option(key=b.nome, text=b.nome))
        self._view.dd_biblioteca.options = opzioni_bib
        opzioni_gen = [ft.dropdown.Option(key="Tutti", text="Tutti")]
        for g in self._model.get_generi():
            opzioni_gen.append(ft.dropdown.Option(key=g, text=g))
        self._view.dd_genere.options = opzioni_gen

        self._view.update()

    # CALLBACKS DROPDOWN
    def cambio_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def cambio_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.lv_libri.controls.clear()
        if not libri:
            self._view.lv_libri.controls.append(ft.Text("Nessun libro trovato."))
        else:
            for libro in libri:
                testo = f"{libro.titolo} - {libro.autore} ({libro.anno_pubblicazione}) [{libro.genere}]"
                self._view.lv_libri.controls.append(ft.Text(testo))
        self._view.update()
