bot.send_message(message.chat.id,f"Done Login : @{username}")
                                head = {
                                     
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                "accept-language": "en-US,en;q=0.9",
                                "content-length": "76",
                                "content-type": "application/x-www-form-urlencoded",
                                "cookie": f'ds_user_id={gett.cookies["ds_user_id"]}; sessionid={sessinoid}; rur="LDC\054250724547\0541703345448:01f799e0351265bfe54c4871f1c5de2f5be38a9c11dc265cadd7c6852315bc0b6ecf5e86"',
                                "origin": "https://www.instagram.com",
                                "referer": "https://www.instagram.com/terms/unblock/?next=/api/v1/web/fxcal/ig_sso_users/",
                                "sec-ch-prefers-color-scheme": "light",
                                "sec-ch-ua": """Not?A_Brand"";v=""8"", ""Chromium"";v=""108"", ""Google Chrome"";v=""108""",
                                "sec-ch-ua-mobile": "?0",
                                "sec-ch-ua-platform": """Windows""",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                "viewport-width": "453",
                                "x-asbd-id": "198387",
                                "x-csrftoken": "m2kPFuLMBSGix4E8ZbRdIDyh0parUk5r",
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "hmac.AR2BpT3Q3cBoHtz_yRH8EvKCYkOb7loHvR4Jah_iP8s8BmTf",
                                "x-instagram-ajax": "9080db6b6a51",
                                "x-requested-with": "XMLHttpRequest",

                                
                            }
                                data1 = "updates=%7B%22existing_user_intro_state%22%3A2%7D&current_screen_key=qp_intro"
                                data = "updates=%7B%22tos_data_policy_consent_state%22%3A2%7D&current_screen_key=tos"
                                requ = requests.post("https://www.instagram.com/web/consent/update/",headers=head,data=data1).text
                                requ1 = requests.post("https://www.instagram.com/web/consent/update/",headers=head,data=data).text
                                print(requ)
                                print(requ1)
                                if '{"screen_key":"finished","status":"ok"}' in requ or '{"screen_key":"finished","status":"ok"}' in requ1:
                                    bot.send_message(message.chat.id,f"Done Accept Terms : @{username}")
                                else:
                                    bot.send_message(message.chat.id,f"Somthing Went Wrong !")
                            except:
                                bot.send_message(message.chat.id,"Invalid Sessionid1")
                        else:
                            bot.send_message(message.chat.id,"Invalid Sessionid")
                except:
                        bot.send_message(message.chat.id,"Invalid Sessionid")
def accept_terms(message):
    global username,accept
    accept = True
    bot.send_message(message.chat.id,"Enter Sessionid ")
    bot.register_next_step_handler(message,accept_term)
def about(message):
    bot.send_message(message.chat.id,f"@QQQ2Q - To request a special copy, contact the developer")
def active():
    global ids
    try:
            scan = requests.get("").text
            ids = scan
    except:
        pass
bot.infinity_polling()