import discord


class ApplySelector(discord.ui.View):
    @discord.ui.select(
        placeholder="Select a role to apply",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Developer",
                description="Apply for developer",
                value='developer'
            ),
            discord.SelectOption(
                label="Content",
                description="Apply for content",
                value='content'
            ),
            discord.SelectOption(
                label="builder",
                description="Apply for builder",
                value='builder'
            ),
            discord.SelectOption(
                label="Supporter",
                description="Apply for supporter",
                value='supporter'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):
        await interaction.response.send_modal(ApplyModal(title=f'Apply for {select.values[0]}'))


class ApplyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="What is your name?"))
        self.add_item(discord.ui.InputText(label="How old are you?"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):

        channel = interaction.channel.guild.get_channel(
            interaction.channel_id
        )
        print(channel.name)

        await channel.create_thread(name="Thread Name", message=None, auto_archive_duration=60, type=None, reason=None)

        # embed = discord.Embed(title="Modal Results")
        # embed.add_field(name="Short Input", value=self.children[0].value)
        # embed.add_field(name="Long Input", value=self.children[1].value)
        # message = await interaction.response.send_message(embeds=[embed])

        # await message.create_thread(name="Results", target=self)
