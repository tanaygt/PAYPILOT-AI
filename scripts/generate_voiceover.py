import asyncio
from pathlib import Path
import edge_tts

OUT = Path('demo_video_assets')
VOICE = 'en-US-AriaNeural'
CLIPS = [
    'PayPilot AI is a purchasing agent for small teams. It turns a plain-English request into a verified plan while humans keep control of every payment.',
    'Tell the agent what your team needs, how many items you need, your budget, and what matters most. There are no complicated procurement forms.',
    'The AI matches your request to a server-owned catalogue. For this example, two monitors and one ergonomic chair total five hundred ninety-seven dollars, leaving three dollars in the budget.',
    'Before payment, you review the products, quantities, prices, and budget status. The AI recommends. PayPilot never authorizes or captures a payment by itself.',
    'After approval, PayPal Sandbox processes the order. PayPilot verifies the completed capture on the server and saves the transaction for an auditable history.',
    'PayPilot AI is controlled agentic commerce: faster procurement, transparent recommendations, and human authorization for every payment.',
]

async def main():
    OUT.mkdir(exist_ok=True)
    for i, text in enumerate(CLIPS, 1):
        out = OUT / f'voice-{i:02d}.mp3'
        await edge_tts.Communicate(text, VOICE, rate='-8%', volume='+0%').save(str(out))
    print(f'Created {len(CLIPS)} voice clips in {OUT.resolve()}')

asyncio.run(main())
