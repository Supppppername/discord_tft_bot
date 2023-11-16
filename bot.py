import discord
from discord.ext import commands

token = "MTE3NDUyMDk3NDg0MzA2MDI2NA.GFOq6f.z47rXopNN3XWQHA8dBZ9stHukhm4vpeoYeovTY"

intents = discord.Intents.default()
intents.message_content = True
data = [["银","银","金",5],["银","银","彩",5],["银","金","金",12],["金","银","金",18],["金","金","彩",3],["金","银","彩",2],
        ["彩","银","金",4],["彩","彩","彩",1],["彩","金","金",2],["银","金","彩",5],["金","金","金",22],["彩","银","彩",1],
        ["银","彩","彩",1],["金","彩","金",10],["金","彩","彩",1],["彩","金","彩",1],["金","彩","银",6],["彩","彩","金",1]]


bot = commands.Bot(command_prefix="！", intents = intents)

class PlayView(discord.ui.View):

    def __init__(self, retVal):
        super().__init__()
        self.retVal = retVal

    def get_choice(self, label):
        return self.retVal + f"{label} "

    def get_prob(self):
        if self.retVal is None or self.retVal== "":
            return "银:28% \n金:62% \n彩:10%"
        if len(self.retVal) == 2:
            temp = {"银": 0, "金":0, "彩":0}
            for i in data:
                if i[0] == self.retVal[0]:
                    temp[i[1]] += i[3]
            total = temp["银"]+temp["金"]+temp["彩"]
            if total == 0:
                return "此种情况不可能出现"
            silver = round(temp["银"]/total*100)
            gold = round(temp["金"] / total*100)
            color = round(temp["彩"] / total*100)
            return f"银:{silver}%\n金:{gold}%\n彩:{color}%"

        if len(self.retVal) == 4:
            temp = {"银": 0, "金":0, "彩":0}
            for i in data:
                if i[0] == self.retVal[0] and i[1] == self.retVal[2]:
                    temp[i[2]] += i[3]
            total = temp["银"]+temp["金"]+temp["彩"]
            if total == 0:
                return "此种情况不可能出现"
            silver = round(temp["银"]/total*100)
            gold = round(temp["金"] / total*100)
            color = round(temp["彩"] / total*100)
            return f"银:{silver}%\n金:{gold}%\n彩:{color}%"

        if len(self.retVal) == 6:
            for i in data:
                if i[0] == self.retVal[0] and i[1] == self.retVal[2] and i[2] == self.retVal[4]:
                    return f"此种情况出现的概率为:{i[3]}%"
            return "此种情况不可能出现"

        return "此种情况不可能出现"



    @discord.ui.button(label="银", style=discord.ButtonStyle.grey)
    async def silver(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_choice(button.label), view=PlayView(self.get_choice(button.label)))

    @discord.ui.button(label="金", style=discord.ButtonStyle.grey)
    async def gold(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_choice(button.label), view=PlayView(self.get_choice(button.label)))

    @discord.ui.button(label="彩", style=discord.ButtonStyle.grey)
    async def color(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_choice(button.label), view=PlayView(self.get_choice(button.label)))

    @discord.ui.button(label="计算", style=discord.ButtonStyle.green)
    async def calculate(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=self.get_prob(), view=None)


@bot.hybrid_command()
async def 海克斯(ctx):
    await ctx.send(view = PlayView(""))

bot.run(token)

