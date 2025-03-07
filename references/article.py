from nicegui import ui

class ArticleRetrieval:

    def __init__(self):

        self.page_title = "Article Retrieval"
        self.headers()
        
        self.stepper = ui.stepper().props("vertical").classes("w-full")

        self.step2_title = "Add optional arguments"
        self.step3_title = "Retrieve articles"

        self.variants_uploaded = False
        self.variants_text = None

        self.keywords_uploaded = False
        self.keywords_text = None
        self.seed = None
        
        self.min_articles = None
        self.max_articles = None
        self.range = None
        self.limit = None

        self.positive_integer_validator = {
            "You can only insert a non-negative integer": self._acceptable_num
        }
    
    def _acceptable_num(self, n) -> bool:
        return (n is None) or (n == int(n) and n >=0)
    
    def _update_seed(self, e):
        self.seed = e.value
        self._step2_next_button_visibility()

    def _update_min_articles(self, e):
        self.min_articles = e.value
        self._step2_next_button_visibility()

    def _update_max_articles(self, e):
        self.max_articles = e.value
        self._step2_next_button_visibility()

    def _update_range(self, e):
        self.range = e.value
        self._step2_next_button_visibility()

    def _update_limit(self, e):
        self.limit = e.value
        self._step2_next_button_visibility()

    def _step2_next_button_visibility(self):
        if all(self._acceptable_num(x) for x in [self.seed, self.min_articles, self.max_articles, self.max_articles, self.limit]):
            self.step2_next_button.set_visibility(True)
        else:
            self.step2_next_button.set_visibility(False)

    def _ask_confirm(self):
        self.md = ui.markdown(
            f"""
            ##### DO YOU CONFIRM THIS DATA?<br>

            **variants**: {self.variants_text}<br>
            **keywords**: {self.keywords_text}<br>
            **seed**: {self.seed}<br>
            **min\\_articles**: {self.min_articles}<br>
            **max\\_articles**: {self.max_articles}<br>
            **range**: {self.range}<br>
            **limit**: {self.limit}<br>
            """
        )

    def headers(self):
        ui.page_title(self.page_title)
        ui.markdown(f"#{self.page_title}")
    
    def step2(self):

        with ui.step(self.step2_title):
            
            ui.number(label="Seed",             validation=self.positive_integer_validator, on_change=self._update_seed        ).props("clearable")
            ui.number(label="Minimum articles", validation=self.positive_integer_validator, on_change=self._update_min_articles).props("clearable")
            ui.number(label="Maximum articles", validation=self.positive_integer_validator, on_change=self._update_max_articles).props("clearable")
            ui.number(label="Range",            validation=self.positive_integer_validator, on_change=self._update_range       ).props("clearable")
            ui.number(label="Limit",            validation=self.positive_integer_validator, on_change=self._update_limit       ).props("clearable")

            with ui.stepper_navigation():
                self.step2_back_button = ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                self.step2_next_button = ui.button("NEXT", icon="arrow_forward_ios", on_click=self.update_markdown_content)
                self.step2_next_button.visibility = False

    def step3(self):
        with ui.step(self.step3_title):
            self._ask_confirm()
            with ui.stepper_navigation():
                ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                ui.button("RUN", icon="rocket_launch", on_click=lambda x: None)  # HERE I WILL PERFORM THE ACTUAL JOB
            return
    
    def update_markdown_content(self):
        self.md.set_content(
            f"""
            ##### DO YOU CONFIRM THIS DATA?<br>

            **variants**: {self.variants_text}<br>
            **keywords**: {self.keywords_text}<br>
            **seed**: {self.seed}<br>
            **min\\_articles**: {self.min_articles}<br>
            **max\\_articles**: {self.max_articles}<br>
            **range**: {self.range}<br>
            **limit**: {self.limit}<br>
            """
            )
        self.stepper.next()

    def run(self):
        with self.stepper:
            self.step2()
            self.step3()
        ui.run()

ArticleRetrieval().run()