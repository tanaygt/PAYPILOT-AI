$ErrorActionPreference = 'Stop'
$out = Join-Path (Get-Location) 'demo_video_assets'
New-Item -ItemType Directory -Force -Path $out | Out-Null
Add-Type -AssemblyName System.Speech

$clips = @(
  'PayPilot AI is a purchasing agent for small teams. It turns a plain-English request into a verified plan while humans keep control of every payment.',
  'Tell the agent what your team needs, how many items you need, your budget, and what matters most. There are no complicated procurement forms.',
  'The AI matches your request to a server-owned catalogue. For this example, two monitors and one ergonomic chair total five hundred ninety-seven dollars, leaving three dollars in the budget.',
  'Before payment, you review the products, quantities, prices, and budget status. The AI recommends. PayPilot never authorizes or captures a payment by itself.',
  'After approval, PayPal Sandbox processes the order. PayPilot verifies the completed capture on the server and saves the transaction for an auditable history.',
  'PayPilot AI is controlled agentic commerce: faster procurement, transparent recommendations, and human authorization for every payment.'
)

$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voice.Rate = 0
$voice.Volume = 100
for ($i=0; $i -lt $clips.Count; $i++) {
  $path = Join-Path $out ("voice-{0:D2}.wav" -f ($i + 1))
  $voice.SetOutputToWaveFile($path)
  $voice.Speak($clips[$i])
  $voice.SetOutputToNull()
}
$voice.Dispose()

$srt = @"
1
00:00:00,000 --> 00:00:20,000
PayPilot AI is a purchasing agent for small teams. It turns a plain-English request into a verified plan while humans keep control of every payment.

2
00:00:20,000 --> 00:00:40,000
Tell the agent what your team needs, how many items you need, your budget, and what matters most. There are no complicated procurement forms.

3
00:00:40,000 --> 00:01:00,000
The AI matches your request to a server-owned catalogue. Two monitors and one ergonomic chair total $597, leaving $3 in the budget.

4
00:01:00,000 --> 00:01:20,000
Before payment, you review the products, quantities, prices, and budget status. The AI recommends. PayPilot never authorizes or captures a payment by itself.

5
00:01:20,000 --> 00:01:40,000
After approval, PayPal Sandbox processes the order. PayPilot verifies the completed capture on the server and saves the transaction for an auditable history.

6
00:01:40,000 --> 00:02:00,000
PayPilot AI is controlled agentic commerce: faster procurement, transparent recommendations, and human authorization for every payment.
"@
$srt | Set-Content (Join-Path $out 'PayPilot-AI-Demo.srt') -Encoding utf8
Write-Output "Created voice clips and subtitles in $out"
