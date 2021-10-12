import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("수업")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send(f"{message.author.name}님, 어서와!")
    if message.content.startswith("하이요"):
        await message.channel.send(f"{message.author.name}님, 어서와요 !")
    if message.content.startswith("응암"):
        await message.channel.send("저리 가서 벽보고 서있어 !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if message.content.startswith("카이스트"):
        await message.channel.send("정말 카이스트 나온거 맞니 ,, ?")
    if message.content.startswith("애시"):
        await message.channel.send("애당아 게임 그만해 ,,")
    if message.content.startswith("쥬댕"):
        await message.channel.send("쥬둥아리 닥쳐라 ,, ^^")
    if message.content.startswith("ㅎㅇ"):
        await message.channel.send(f"{message.author.name}님, 어서왕ㅋ")
    if message.content.startswith("프로봇"):
        await message.channel.send("너 쫌 질투나")
    if message.content.startswith("쌤"):
        await message.channel.send("세상에서 확마가 제일 예뿌 !")
    if message.content.startswith("확마"):
        await message.channel.send("어떻게 이렇게 예뿌지 ,, ?")
    if message.content.startswith("주우땡"):
        await message.channel.send("어서와요 신입ㅋ")
    if message.content.startswith("진북"):
        await message.channel.send("최전방 다녀온 우리 진북이 ,,")
    if message.content.startswith("평양"):
        await message.channel.send("내레 북조선에 있을 땐 마리야 김정은 동지가 아쥬 체고였지 기레 ,, 남조선을 향해 대포동 미사일 발싸아아아ㅏ아아")
    if message.content.startswith("전데용"):
        await message.channel.send("이게 ~~~~~~ 전데용 ??")
    if message.content.startswith("ai"):
        await message.channel.send("너가 사람이야 ?")
    if message.content.startswith("방패"):
        await message.channel.send("하루 종일도 할 수 있어 ,, !")
    if message.content.startswith("파국"):
        await message.channel.send("이것이 파국이니라 ,, ")
    if message.content.startswith("논현동"):
        await message.channel.send("그래서 여기 땅값이 얼마라고 ?")
    if message.content.startswith("친구"):
        await message.channel.send("내가 니 친구냐 ? 너 안경 벗어봐")
    if message.content.startswith("도박"):
        await message.channel.send("싸늘하다 ,, 찌찌에 비수가 날아와 꽂힌다 ,, 하지만 걱정하지마라 ,, 손은 눈보다 빠르니깐 ,,,,")
    if message.content.startswith("ㅋ"):
        await message.channel.send(f"{message.author.name}님, 웃어 ? {message.author.name}는 지금 이 상황이 웃겨 ?")
    if message.content.startswith("사랑해"):
        await message.channel.send(f"{message.author.name}님, 나 좋아하지마 ,, 우린 그져 선생과 학생의 관계일 뿐이라구 !!")
    if message.content.startswith("어서오세요"):
        await message.channel.send(f"{message.author.name}님, 어서오세요 ! 정말 좋은 하루에요 !!")
    if message.content.startswith("뚜이"):
        await message.channel.send("라따뚜이 고놈이 음식은 참 잘했지 그래 ,, 쥐덫이 어딨더라 ,,, ?")
    if message.content.startswith("라마시아"):
        await message.channel.send("바르샤의 전개는 환상적이긴 하지 ,, 근데 메슬렁은 참지 못해")
    if message.content.startswith("레이"):
        await message.channel.send("레이 그 백정놈이 ,, 지 형 죽인 놈 찾겠다고 피를 뿌리고 다닌다던데 ,, 사람을 반으로 갈라 창자를 꺼낸다지 ?")
    if message.content.startswith("갱단주"):
        await message.channel.send("Guzzi gang Guzzi gang Guzzi gang 내가 사실 한 때는 라스베가스 총잽이였지 ,, 총알이 두 개지요오오오오ㅗ오옹")
    if message.content.startswith("안뇽"):
        await message.channel.send(f"{message.author.name}님, 안녕하세요 반갑습니다 !")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
