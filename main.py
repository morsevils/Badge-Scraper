from exeouv.scraper import scrape
from colorama import Fore, Style
from pystyle import Center, Colors, Colorate
import json

x = [
    "f",
    "F",
    "n",
    "N"
]


print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""

                                                            
                                        ┏━ ┏━┃┏━┃┃ ┃━┏┛┃ ┃
                                        ┃ ┃┏┏┛┏━┃ ┛  ┃ ━┏┛
                                        ━━ ┛ ┛┛ ┛┛ ┛ ┛  ┛     
                      ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                      ┇              [Discord] teshcik                      ┇
                      ┇                              
                      ┇                                                    ┇
                      ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                      

                      
                      """)))

def main():

    token = input(f"{Fore.CYAN}Hesabin Tokenini giriniz. (config dosyasına girdiyseniz enter basarak atlayiniz.): {Style.RESET_ALL}")

    if len(token) < 10:
        with open("config.json", "r", encoding="utf-8") as ff:
            config = json.load(ff)
            token = config["token"]

    guild_id = input(F"{Fore.CYAN}Sunucu idsini giriniz: {Style.RESET_ALL}")
    channel_id = input(F"{Fore.CYAN}Sunucudaki herhangi bir Kanal idsini giriniz: {Style.RESET_ALL}")

    run_badge_scraper = input(f"{Fore.CYAN}Badge scraperi calistir? ({Style.RESET_ALL}y{Fore.CYAN}/{Style.RESET_ALL}n{Fore.CYAN})?{Style.RESET_ALL} ")

    if run_badge_scraper != "n" or run_badge_scraper != "y":
        for y in x:
            if y in run_badge_scraper:
                run_badge_scraper = "n"
                break
            else:
                run_badge_scraper = "y"
    run_badge_scraper = bool(run_badge_scraper)

    member_data = scrape(token, guild_id, channel_id, run_badge_scraper)

    with open(f"scraped/{guild_id}.txt", "w", encoding="utf-8") as f:
        for member in member_data.values():
            id = member['id']
            tag = member['tag']
            badges = ','.join(member.get('badges', []))
            f.write(f"ID: {id} | Username: {tag} | Badges: {badges}\n")

    print(f"{Fore.LIGHTGREEN_EX}[SUCCESS]{Style.RESET_ALL} {Fore.GREEN}Başarıyla {len(member_data)} Kisi {guild_id} sunucusundan cekildi ve kaydedildi./{guild_id}.txt {Style.RESET_ALL}")
    input("Cikis yapmak icin ENTERa basiniz.\n\n")

main()
