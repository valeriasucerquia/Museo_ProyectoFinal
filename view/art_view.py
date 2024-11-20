class ArtView:
    def display_message(self, message):
        print(message)

    def display_artwork(self, artwork):
        if isinstance(artwork, dict):
            for key, value in artwork.items():
                print(f"{key}: {value}")
        else:
            print(artwork)

    def prompt_for_input(self, prompt_text):
        return input(prompt_text)
