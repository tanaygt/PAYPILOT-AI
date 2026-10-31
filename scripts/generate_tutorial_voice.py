import asyncio
from pathlib import Path
import edge_tts

OUT=Path('tutorial_video_assets'); OUT.mkdir(exist_ok=True)
VOICE='en-US-AriaNeural'
CLIPS=[
 'First, we load PayPilot. The dashboard starts with zero verified spend because the application never fabricates payment data. This is our health and empty-state test.',
 'Next, we test a real purchasing brief. The user asks for two monitors and one office chair with a six-hundred-dollar budget. The request is sent to the server.',
 'The AI matches the request to the server catalogue. It returns two Acer monitors and one Branch chair for five hundred ninety-seven dollars, leaving three dollars in budget.',
 'Now we run a negative test. Increasing the quantity pushes the total above the budget. PayPilot blocks the payment button and sends nothing to PayPal.',
 'With a valid plan, the human approval screen appears. The PayPal Sandbox button is rendered only after review, and the server recalculates prices before creating an order.',
 'We test both checkout outcomes. Cancelled checkout is not success. Approved checkout becomes success only when PayPal returns a completed capture and a capture reference.',
 'Finally, we open transaction history. The verified amount, PayPal identifiers, and status are persisted for audit. This completes the PayPilot journey: plan, guardrail, approval, capture, and accountability.'
]
async def main():
 for i, text in enumerate(CLIPS,1): await edge_tts.Communicate(text,VOICE,rate='-8%').save(str(OUT/f'voice-{i:02d}.mp3'))
 print('Generated tutorial voiceover')
asyncio.run(main())
