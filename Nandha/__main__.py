from Nandha import Nandha


if __name__ == "__main__":
    Nandha.run()
    with Nandha:
        Nandha.send_message(config.GROUP_ID, "`hello every your group protection system alive!`")
