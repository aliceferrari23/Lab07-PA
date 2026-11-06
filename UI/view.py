import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd_biblioteca = ft.Dropdown(label="Biblioteca", on_select=self.controller.cambio_biblioteca, expand=True)
        self.dd_genere = ft.Dropdown(label="Genere", on_select=self.controller.cambio_genere, expand=True)

        self.row_filtri = ft.Row(controls=[self.dd_biblioteca, self.dd_genere], alignment=ft.MainAxisAlignment.CENTER)

        # Sezione 3: Libri
        self.btn_mostra = ft.Button(content="Mostra Libri", on_click=self.controller.handle_mostra_libri)
        self.row_bottone = ft.Row(controls=[self.btn_mostra], alignment=ft.MainAxisAlignment.CENTER)

        self.lv_libri = ft.ListView(expand=1, spacing=10, padding=20)
        self.container_libri = ft.Container(content=self.lv_libri, expand=True)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            self.row_filtri,
            ft.Divider(),

            # Sezione 3: Libri
            self.row_bottone,
            self.container_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()
        if self.controller is not None:
            self.controller.popola_dropdowns()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
