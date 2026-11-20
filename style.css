<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NVIDIA NetQ | Fabric Telemetry & Deployment Automation</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        nvidia: {
                            green: '#76B900',
                            darkGreen: '#5a8f00',
                            lightGreen: '#8cd400',
                            black: '#0A0D10',
                            surface: '#11161D',
                            card: '#161C24',
                            border: '#242E3B',
                            muted: '#8A99AD'
                        }
                    }
                }
            }
        }
    </script>

    <style>
        /* Custom Scrollbar & Subtle Hardware-Accelerated Animations */
        body {
            background-color: #0A0D10;
            color: #F1F5F9;
            overflow-x: hidden;
        }
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0A0D10;
        }
        ::-webkit-scrollbar-thumb {
            background: #242E3B;
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #76B900;
        }
        .nvidia-glow {
            box-shadow: 0 0 20px rgba(118, 185, 0, 0.15);
        }
        .nvidia-border-glow:hover {
            border-color: rgba(118, 185, 0, 0.6);
            box-shadow: 0 0 15px rgba(118, 185, 0, 0.2);
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.95); opacity: 0.8; }
            70% { transform: scale(1.25); opacity: 0; }
            100% { transform: scale(1.25); opacity: 0; }
        }
        .pulse-dot::before {
            content: '';
            position: absolute;
            inset: -3px;
            border-radius: 50%;
            background-color: inherit;
            animation: pulse-ring 2s cubic-bezier(0.24, 0, 0.38, 1) infinite;
        }
        .topo-link {
            transition: stroke 0.3s ease, stroke-width 0.3s ease, opacity 0.3s ease;
        }
        .topo-link-active {
            stroke: #76B900 !important;
            stroke-width: 3.5 !important;
            stroke-dasharray: 8 4;
            animation: dashFlow 1s linear infinite;
        }
        @keyframes dashFlow {
            to { stroke-dashoffset: -12; }
        }
        .tab-panel {
            animation: fadeIn 0.25s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col font-sans antialiased selection:bg-nvidia-green selection:text-black">

    <!-- Toast Notification Container (Replaces alert) -->
    <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-nvidia-surface/95 backdrop-blur-md border-b border-nvidia-border">
        <div class="max-w-[1600px] mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-wrap items-center justify-between h-auto py-3 md:py-0 md:h-16 gap-3">
                
                <!-- Brand & Fabric Context -->
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-lg bg-nvidia-green flex items-center justify-center text-black font-extrabold text-lg shadow-lg shadow-nvidia-green/20">
                        <i class="fa-solid fa-network-wired"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-bold tracking-tight text-white text-base sm:text-lg">NVIDIA <span class="text-nvidia-green">NetQ</span></span>
                            <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-nvidia-green/15 text-nvidia-green border border-nvidia-green/30">
                                v4.12.0 Enterprise
                            </span>
                        </div>
                        <p class="text-[11px] text-nvidia-muted font-mono">Fabric: <span class="text-slate-300">us-west-ai-pod01</span> • Spectrum-X / Cumulus 5.9 & SONiC</p>
                    </div>
                </div>

                <!-- Navigation Tabs -->
                <nav class="flex items-center gap-1 bg-nvidia-black/70 p-1 rounded-xl border border-nvidia-border overflow-x-auto max-w-full" role="tablist">
                    <button onclick="switchTab('telemetry')" id="tab-btn-telemetry" class="nav-tab active-tab flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs sm:text-sm font-medium transition-all whitespace-nowrap bg-nvidia-green text-black font-semibold shadow">
                        <i class="fa-solid fa-chart-line"></i>
                        <span>Live Telemetry & Fabric</span>
                    </button>
                    <button onclick="switchTab('automation')" id="tab-btn-automation" class="nav-tab flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs sm:text-sm font-medium text-slate-400 hover:text-white hover:bg-nvidia-card transition-all whitespace-nowrap">
                        <i class="fa-solid fa-code-branch"></i>
                        <span>ZTP & CI/CD Automation</span>
                    </button>
                    <button onclick="switchTab('trace')" id="tab-btn-trace" class="nav-tab flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs sm:text-sm font-medium text-slate-400 hover:text-white hover:bg-nvidia-card transition-all whitespace-nowrap">
                        <i class="fa-solid fa-route"></i>
                        <span>Trace & Validation</span>
                    </button>
                    <button onclick="switchTab('reference')" id="tab-btn-reference" class="nav-tab flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs sm:text-sm font-medium text-slate-400 hover:text-white hover:bg-nvidia-card transition-all whitespace-nowrap">
                        <i class="fa-solid fa-terminal"></i>
                        <span>Architecture & CLI</span>
                    </button>
                </nav>

                <!-- Live Streaming Status & Manual Refresh -->
                <div class="hidden xl:flex items-center gap-3">
                    <div class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-nvidia-black border border-nvidia-border text-xs font-mono">
                        <span class="relative flex h-2 w-2 rounded-full bg-nvidia-green pulse-dot"></span>
                        <span class="text-slate-300">OTel Stream: <strong class="text-nvidia-green">100ms</strong></span>
                    </div>
                    <button onclick="toggleStream()" id="stream-toggle-btn" class="px-3 py-1.5 rounded-lg bg-nvidia-card hover:bg-nvidia-border border border-nvidia-border text-xs font-medium text-slate-200 transition flex items-center gap-1.5">
                        <i id="stream-icon" class="fa-solid fa-pause text-nvidia-green"></i>
                        <span id="stream-label">Live</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Workspace Container -->
    <main class="flex-1 max-w-[1600px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- ===================================================================== -->
        <!-- TAB 1: LIVE TELEMETRY & FABRIC OVERVIEW                               -->
        <!-- ===================================================================== -->
        <section id="panel-telemetry" class="tab-panel space-y-6">
            
            <!-- Top KPI Summary Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
                <!-- KPI 1: Total Switches -->
                <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-4 nvidia-border-glow transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-medium uppercase tracking-wider text-nvidia-muted">Managed Switches</span>
                        <span class="p-2 rounded-lg bg-slate-800/80 text-nvidia-green text-xs"><i class="fa-solid fa-server"></i></span>
                    </div>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span class="text-2xl font-bold text-white font-mono">12</span>
                        <span class="text-xs text-nvidia-green font-medium">100% Online</span>
                    </div>
                    <p class="mt-1.5 text-[11px] text-slate-400 font-mono">2 Super-Spine • 4 Spine • 6 Leaf</p>
                </div>

                <!-- KPI 2: Fabric Health Score -->
                <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-4 nvidia-border-glow transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-medium uppercase tracking-wider text-nvidia-muted">Fabric Health Score</span>
                        <span class="p-2 rounded-lg bg-nvidia-green/15 text-nvidia-green text-xs"><i class="fa-solid fa-heart-pulse"></i></span>
                    </div>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span id="kpi-health" class="text-2xl font-bold text-nvidia-green font-mono">99.4%</span>
                        <span class="text-xs text-slate-400">+0.2% (24h)</span>
                    </div>
                    <div class="w-full bg-nvidia-black h-1.5 rounded-full mt-2 overflow-hidden">
                        <div class="bg-nvidia-green h-full rounded-full" style="width: 99.4%"></div>
                    </div>
                </div>

                <!-- KPI 3: Active BGP / EVPN Sessions -->
                <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-4 nvidia-border-glow transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-medium uppercase tracking-wider text-nvidia-muted">BGP / EVPN Sessions</span>
                        <span class="p-2 rounded-lg bg-blue-500/15 text-blue-400 text-xs"><i class="fa-solid fa-diagram-project"></i></span>
                    </div>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span class="text-2xl font-bold text-white font-mono">64 / 64</span>
                        <span class="text-xs text-nvidia-green font-medium">Established</span>
                    </div>
                    <p class="mt-1.5 text-[11px] text-slate-400 font-mono">BGP Unnumbered • VNI 10010-10040</p>
                </div>

                <!-- KPI 4: RoCEv2 Packet Drop Rate -->
                <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-4 nvidia-border-glow transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-medium uppercase tracking-wider text-nvidia-muted">Packet Drop Rate</span>
                        <span class="p-2 rounded-lg bg-purple-500/15 text-purple-400 text-xs"><i class="fa-solid fa-shield-halved"></i></span>
                    </div>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span id="kpi-drops" class="text-2xl font-bold text-white font-mono">0.0002%</span>
                        <span class="text-xs text-nvidia-green font-medium">Lossless</span>
                    </div>
                    <p class="mt-1.5 text-[11px] text-slate-400 font-mono">RoCEv2 ECN Active • 0 PFC Storms</p>
                </div>

                <!-- KPI 5: Active Alerts -->
                <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-4 nvidia-border-glow transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-medium uppercase tracking-wider text-nvidia-muted">Active Alerts</span>
                        <span class="p-2 rounded-lg bg-amber-500/15 text-amber-400 text-xs"><i class="fa-solid fa-bell"></i></span>
                    </div>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span id="kpi-alerts-count" class="text-2xl font-bold text-amber-400 font-mono">3</span>
                        <span class="text-xs text-slate-400">1 Crit • 2 Warn</span>
                    </div>
                    <p class="mt-1.5 text-[11px] text-slate-400 font-mono">Click alarm row below to remediate</p>
                </div>
            </div>

            <!-- Middle Grid: Interactive Clos Topology + Node Inspector & Real-Time Telemetry Charts -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Interactive Clos Topology Visualizer (7 Columns) -->
                <div class="lg:col-span-7 bg-nvidia-card border border-nvidia-border rounded-xl flex flex-col overflow-hidden">
                    <div class="px-5 py-3.5 border-b border-nvidia-border flex flex-wrap items-center justify-between gap-2 bg-nvidia-surface/50">
                        <div>
                            <h2 class="text-sm font-semibold text-white flex items-center gap-2">
                                <i class="fa-solid fa-sitemap text-nvidia-green"></i>
                                Interactive 3-Tier Clos AI Fabric Topology
                            </h2>
                            <p class="text-xs text-nvidia-muted">Click any Super-Spine, Spine, Leaf, or DGX H100 node to inspect ASIC telemetry</p>
                        </div>
                        <div class="flex items-center gap-3 text-[11px] font-mono">
                            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-nvidia-green"></span>Healthy</span>
                            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>Warning</span>
                            <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span>Degraded</span>
                        </div>
                    </div>

                    <!-- Responsive SVG Fabric Canvas -->
                    <div class="relative flex-1 bg-nvidia-black/90 p-3 flex items-center justify-center min-h-[380px]">
                        <svg id="fabric-svg" viewBox="0 0 800 420" class="w-full h-auto max-h-[420px] select-none">
                            <defs>
                                <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
                                    <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#18202C" stroke-width="1"/>
                                </pattern>
                            </defs>
                            <rect width="800" height="420" fill="url(#grid)" />

                            <!-- Tier Labels on Left -->
                            <text x="14" y="48" fill="#64748B" font-size="10" font-family="JetBrains Mono" font-weight="600">SUPER-SPINE</text>
                            <text x="14" y="152" fill="#64748B" font-size="10" font-family="JetBrains Mono" font-weight="600">SPINE (SN5600)</text>
                            <text x="14" y="262" fill="#64748B" font-size="10" font-family="JetBrains Mono" font-weight="600">LEAF (SN5600)</text>
                            <text x="14" y="372" fill="#64748B" font-size="10" font-family="JetBrains Mono" font-weight="600">DGX H100 PODS</text>

                            <!-- Links Layer (Populated by JS) -->
                            <g id="topo-links"></g>

                            <!-- Nodes Layer (Populated by JS) -->
                            <g id="topo-nodes"></g>
                        </svg>
                    </div>
                </div>

                <!-- Right Column: Selected Node ASIC Inspector + Live Telemetry Charts (5 Columns) -->
                <div class="lg:col-span-5 flex flex-col gap-6">
                    
                    <!-- Node Telemetry Inspector Card -->
                    <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-5">
                        <div class="flex items-start justify-between border-b border-nvidia-border pb-3">
                            <div>
                                <div class="flex items-center gap-2">
                                    <span id="insp-badge" class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-nvidia-green/20 text-nvidia-green">HEALTHY</span>
                                    <h3 id="insp-name" class="text-base font-bold text-white font-mono">leaf-01</h3>
                                </div>
                                <p id="insp-model" class="text-xs text-nvidia-muted mt-0.5">NVIDIA Spectrum-4 SN5600 • Cumulus Linux 5.9.1</p>
                            </div>
                            <span id="insp-agent" class="text-[11px] font-mono px-2.5 py-1 rounded bg-nvidia-black border border-nvidia-border text-nvidia-green">
                                netq-agent: UP
                            </span>
                        </div>

                        <!-- Hardware Metrics Grid -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-4">
                            <div class="bg-nvidia-black/80 p-2.5 rounded-lg border border-nvidia-border/70">
                                <span class="text-[10px] text-nvidia-muted uppercase block">ASIC Temp</span>
                                <span id="insp-temp" class="text-sm font-bold font-mono text-white mt-0.5 block">46.2 °C</span>
                            </div>
                            <div class="bg-nvidia-black/80 p-2.5 rounded-lg border border-nvidia-border/70">
                                <span class="text-[10px] text-nvidia-muted uppercase block">Link Util</span>
                                <span id="insp-util" class="text-sm font-bold font-mono text-nvidia-green mt-0.5 block">68.4%</span>
                            </div>
                            <div class="bg-nvidia-black/80 p-2.5 rounded-lg border border-nvidia-border/70">
                                <span class="text-[10px] text-nvidia-muted uppercase block">Active Ports</span>
                                <span id="insp-ports" class="text-sm font-bold font-mono text-white mt-0.5 block">62 / 64 UP</span>
                            </div>
                            <div class="bg-nvidia-black/80 p-2.5 rounded-lg border border-nvidia-border/70">
                                <span class="text-[10px] text-nvidia-muted uppercase block">Buffer Peak</span>
                                <span id="insp-buffer" class="text-sm font-bold font-mono text-blue-400 mt-0.5 block">18.5%</span>
                            </div>
                        </div>

                        <!-- Interface Breakdown Bar -->
                        <div class="mt-4">
                            <div class="flex justify-between text-[11px] font-mono text-slate-400 mb-1">
                                <span>800GbE / 400GbE Port State Summary</span>
                                <span id="insp-ip" class="text-slate-300">Loopback: 10.255.0.11/32</span>
                            </div>
                            <div id="insp-port-pills" class="flex flex-wrap gap-1.5 mt-2">
                                <!-- Dynamic port badges -->
                            </div>
                        </div>
                    </div>

                    <!-- Real-Time Streaming Charts (Canvas) -->
                    <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-5 flex-1 flex flex-col justify-between">
                        <div class="flex items-center justify-between mb-3">
                            <div>
                                <h3 class="text-sm font-semibold text-white">Real-Time Fabric Telemetry (What Just Happened)</h3>
                                <p class="text-[11px] text-nvidia-muted">East-West RoCEv2 Bandwidth (Tbps) & ECN Marking Rate</p>
                            </div>
                            <div class="flex items-center gap-3 text-[11px] font-mono">
                                <span class="flex items-center gap-1 text-nvidia-green"><span class="w-2 h-2 rounded-full bg-nvidia-green"></span>BW (Tbps)</span>
                                <span class="flex items-center gap-1 text-cyan-400"><span class="w-2 h-2 rounded-full bg-cyan-400"></span>Buffer %</span>
                            </div>
                        </div>
                        <div class="relative w-full h-40 bg-nvidia-black/80 rounded-lg border border-nvidia-border/70 p-2">
                            <canvas id="telemetry-chart" class="w-full h-full block"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Bottom Section: Interactive Alarm & Event Log Table -->
            <div class="bg-nvidia-card border border-nvidia-border rounded-xl overflow-hidden">
                <div class="px-5 py-3.5 border-b border-nvidia-border flex flex-wrap items-center justify-between gap-3 bg-nvidia-surface/50">
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-triangle-exclamation text-amber-400"></i>
                        <h3 class="text-sm font-semibold text-white">NetQ Event & Anomaly Stream</h3>
                    </div>
                    <!-- Severity Filters -->
                    <div class="flex items-center gap-1.5">
                        <button onclick="filterAlarms('ALL')" class="alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-green text-black font-semibold" data-filter="ALL">All Events</button>
                        <button onclick="filterAlarms('CRITICAL')" class="alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-black text-slate-300 border border-nvidia-border hover:border-rose-500/50" data-filter="CRITICAL">Critical</button>
                        <button onclick="filterAlarms('WARNING')" class="alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-black text-slate-300 border border-nvidia-border hover:border-amber-500/50" data-filter="WARNING">Warning</button>
                        <button onclick="filterAlarms('INFO')" class="alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-black text-slate-300 border border-nvidia-border hover:border-blue-500/50" data-filter="INFO">Info</button>
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-nvidia-border bg-nvidia-black/50 text-[11px] font-mono uppercase text-nvidia-muted">
                                <th class="py-3 px-4">Timestamp</th>
                                <th class="py-3 px-4">Severity</th>
                                <th class="py-3 px-4">Node / Interface</th>
                                <th class="py-3 px-4">Telemetry Event & Root Cause</th>
                                <th class="py-3 px-4 text-right">Action</th>
                            </tr>
                        </thead>
                        <tbody id="alarms-tbody" class="divide-y divide-nvidia-border/60 text-xs">
                            <!-- Populated via JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ===================================================================== -->
        <!-- TAB 2: DEPLOYMENT AUTOMATION (ZTP & CI/CD PIPELINE)                   -->
        <!-- ===================================================================== -->
        <section id="panel-automation" class="tab-panel hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Left Configuration Panel (5 Columns) -->
                <div class="lg:col-span-5 bg-nvidia-card border border-nvidia-border rounded-xl p-5 space-y-5">
                    <div class="border-b border-nvidia-border pb-3">
                        <h2 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-robot text-nvidia-green"></i>
                            NetQ GitOps & ZTP Orchestrator
                        </h2>
                        <p class="text-xs text-nvidia-muted mt-0.5">Declarative NVUE / SONiC rollout with automated NetQ validation gates</p>
                    </div>

                    <!-- Step 1: Select Target Switches -->
                    <div>
                        <label class="block text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">
                            1. Select Target Fabric Nodes
                        </label>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2" id="target-switches-grid">
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-green/60 text-xs font-mono text-white">
                                <input type="checkbox" value="leaf-01" checked onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>leaf-01</span>
                            </label>
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-green/60 text-xs font-mono text-white">
                                <input type="checkbox" value="leaf-02" checked onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>leaf-02</span>
                            </label>
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-border text-xs font-mono text-slate-300">
                                <input type="checkbox" value="leaf-03" onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>leaf-03</span>
                            </label>
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-border text-xs font-mono text-slate-300">
                                <input type="checkbox" value="spine-01" onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>spine-01</span>
                            </label>
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-border text-xs font-mono text-slate-300">
                                <input type="checkbox" value="spine-02" onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>spine-02</span>
                            </label>
                            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-lg bg-nvidia-black border border-nvidia-border text-xs font-mono text-slate-300">
                                <input type="checkbox" value="superspine-01" onchange="updatePlaybookPreview()" class="accent-[#76B900] rounded">
                                <span>sspine-01</span>
                            </label>
                        </div>
                    </div>

                    <!-- Step 2: Choose Automation Playbook -->
                    <div>
                        <label for="playbook-select" class="block text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">
                            2. Choose Automation Playbook
                        </label>
                        <select id="playbook-select" onchange="updatePlaybookPreview()" class="w-full bg-nvidia-black border border-nvidia-border rounded-lg px-3.5 py-2.5 text-xs sm:text-sm text-white font-medium focus:outline-none focus:border-nvidia-green">
                            <option value="evpn">EVPN-VXLAN Anycast Gateway & BGP Unnumbered Provisioning</option>
                            <option value="rocev2">Spectrum-X RoCEv2 Lossless QoS, ECN & PFC Buffer Tuning</option>
                            <option value="ztp">Zero-Touch Provisioning (ZTP) + Cumulus Linux 5.9 Image Upgrade</option>
                        </select>
                    </div>

                    <!-- Step 3: NetQ Canary & Auto-Rollback Policy -->
                    <div class="bg-nvidia-black/70 border border-nvidia-border rounded-lg p-3.5 space-y-2.5">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-semibold text-white">NetQ Pre/Post Validation Gate</span>
                            <span class="text-[11px] font-mono text-nvidia-green">Auto-Rollback: ENABLED</span>
                        </div>
                        <p class="text-[11px] text-slate-400">
                            Automatically snapshots fabric state via <code class="text-slate-200">netq check</code> before push and reverts NVUE revision if BGP/EVPN sessions or MTU checks degrade.
                        </p>
                    </div>

                    <!-- Execute Pipeline CTA -->
                    <button id="run-pipeline-btn" onclick="runDeploymentPipeline()" class="w-full py-3 px-4 rounded-xl bg-nvidia-green hover:bg-nvidia-lightGreen text-black font-bold text-sm shadow-lg shadow-nvidia-green/20 transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-play"></i>
                        <span>Run Deployment Pipeline</span>
                    </button>
                </div>

                <!-- Right Panel: YAML/NVUE Preview + Animated CI/CD Pipeline & Live Console (7 Columns) -->
                <div class="lg:col-span-7 flex flex-col gap-6">
                    
                    <!-- Pipeline Stage Stepper -->
                    <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-5">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-sm font-semibold text-white">CI/CD Execution Pipeline</h3>
                            <span id="pipeline-status-badge" class="px-2.5 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300">READY</span>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
                            <div id="stage-1" class="pipeline-stage p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all">
                                <div class="text-slate-400 text-base mb-1"><i class="fa-brands fa-git-alt"></i></div>
                                <div class="text-[11px] font-bold text-white">1. Git Push</div>
                                <div class="text-[10px] font-mono text-slate-500 mt-0.5 stage-sub">Pending</div>
                            </div>
                            <div id="stage-2" class="pipeline-stage p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all">
                                <div class="text-slate-400 text-base mb-1"><i class="fa-solid fa-clipboard-check"></i></div>
                                <div class="text-[11px] font-bold text-white">2. NetQ Pre-Check</div>
                                <div class="text-[10px] font-mono text-slate-500 mt-0.5 stage-sub">Pending</div>
                            </div>
                            <div id="stage-3" class="pipeline-stage p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all">
                                <div class="text-slate-400 text-base mb-1"><i class="fa-solid fa-cloud-arrow-up"></i></div>
                                <div class="text-[11px] font-bold text-white">3. NVUE Push</div>
                                <div class="text-[10px] font-mono text-slate-500 mt-0.5 stage-sub">Pending</div>
                            </div>
                            <div id="stage-4" class="pipeline-stage p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all">
                                <div class="text-slate-400 text-base mb-1"><i class="fa-solid fa-vial-circle-check"></i></div>
                                <div class="text-[11px] font-bold text-white">4. Post-Validate</div>
                                <div class="text-[10px] font-mono text-slate-500 mt-0.5 stage-sub">Pending</div>
                            </div>
                            <div id="stage-5" class="pipeline-stage col-span-2 sm:col-span-1 p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all">
                                <div class="text-slate-400 text-base mb-1"><i class="fa-solid fa-circle-check"></i></div>
                                <div class="text-[11px] font-bold text-white">5. Commit</div>
                                <div class="text-[10px] font-mono text-slate-500 mt-0.5 stage-sub">Pending</div>
                            </div>
                        </div>
                    </div>

                    <!-- Generated NVUE YAML Preview -->
                    <div class="bg-nvidia-card border border-nvidia-border rounded-xl overflow-hidden">
                        <div class="px-4 py-2.5 bg-nvidia-surface/70 border-b border-nvidia-border flex items-center justify-between">
                            <span class="text-xs font-mono font-semibold text-slate-300"><i class="fa-solid fa-file-code text-nvidia-green mr-1.5"></i>Generated NVUE / NetQ Validation Manifest</span>
                            <button onclick="copyPlaybookCode()" class="text-xs text-slate-400 hover:text-white flex items-center gap-1 px-2 py-1 rounded bg-nvidia-black border border-nvidia-border">
                                <i class="fa-regular fa-copy"></i> Copy YAML
                            </button>
                        </div>
                        <pre id="yaml-preview" class="p-4 text-xs font-mono text-slate-300 bg-nvidia-black/90 overflow-x-auto max-h-52 leading-relaxed"></pre>
                    </div>

                    <!-- Live Execution Console -->
                    <div class="bg-nvidia-card border border-nvidia-border rounded-xl overflow-hidden flex-1 flex flex-col">
                        <div class="px-4 py-2.5 bg-nvidia-surface/70 border-b border-nvidia-border flex items-center justify-between">
                            <span class="text-xs font-mono font-semibold text-slate-300"><i class="fa-solid fa-terminal text-nvidia-green mr-1.5"></i>Ansible / NetQ Runner Console</span>
                            <button onclick="clearPipelineLogs()" class="text-[11px] font-mono text-slate-400 hover:text-white">Clear</button>
                        </div>
                        <div id="pipeline-console" class="p-4 font-mono text-xs bg-[#07090B] text-slate-300 h-48 overflow-y-auto space-y-1.5">
                            <div class="text-slate-500"># Select target switches and playbook, then click "Run Deployment Pipeline"...</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ===================================================================== -->
        <!-- TAB 3: TRACE & VALIDATION ENGINE                                      -->
        <!-- ===================================================================== -->
        <section id="panel-trace" class="tab-panel hidden space-y-6">
            
            <!-- Top Section: Interactive Path Trace Simulator (netq trace) -->
            <div class="bg-nvidia-card border border-nvidia-border rounded-xl p-5 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-2 border-b border-nvidia-border pb-3">
                    <div>
                        <h2 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-route text-nvidia-green"></i>
                            NetQ End-to-End Overlay & Underlay Path Trace (<code class="text-nvidia-green text-sm">netq trace</code>)
                        </h2>
                        <p class="text-xs text-nvidia-muted mt-0.5">Trace VXLAN tunnel encapsulation, ECMP hash path, MTU consistency, and hop-by-hop latency between GPU nodes</p>
                    </div>
                </div>

                <!-- Trace Form Controls -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 items-end">
                    <div>
                        <label class="block text-[11px] font-mono uppercase text-nvidia-muted mb-1">Source Host</label>
                        <select id="trace-src" class="w-full bg-nvidia-black border border-nvidia-border rounded-lg px-3 py-2 text-xs font-mono text-white focus:border-nvidia-green focus:outline-none">
                            <option value="gpu-node-01">gpu-node-01 (10.10.10.11)</option>
                            <option value="gpu-node-02">gpu-node-02 (10.10.10.12)</option>
                            <option value="gpu-node-04">gpu-node-04 (10.10.20.14)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[11px] font-mono uppercase text-nvidia-muted mb-1">Destination Host</label>
                        <select id="trace-dst" class="w-full bg-nvidia-black border border-nvidia-border rounded-lg px-3 py-2 text-xs font-mono text-white focus:border-nvidia-green focus:outline-none">
                            <option value="gpu-node-08">gpu-node-08 (10.10.30.18)</option>
                            <option value="gpu-node-06">gpu-node-06 (10.10.30.16)</option>
                            <option value="gpu-node-03">gpu-node-03 (10.10.20.13)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[11px] font-mono uppercase text-nvidia-muted mb-1">Tenant VRF / VNI</label>
                        <select id="trace-vrf" class="w-full bg-nvidia-black border border-nvidia-border rounded-lg px-3 py-2 text-xs font-mono text-white focus:border-nvidia-green focus:outline-none">
                            <option value="vrf-ai-train (VNI 10010)">vrf-ai-train (VNI 10010)</option>
                            <option value="vrf-storage (VNI 10020)">vrf-storage (VNI 10020)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[11px] font-mono uppercase text-nvidia-muted mb-1">Probe MTU / Protocol</label>
                        <select id="trace-mtu" class="w-full bg-nvidia-black border border-nvidia-border rounded-lg px-3 py-2 text-xs font-mono text-white focus:border-nvidia-green focus:outline-none">
                            <option value="9000">9000 Bytes (RoCEv2 / RDMA)</option>
                            <option value="9216">9216 Bytes (Jumbo VXLAN)</option>
                            <option value="1500">1500 Bytes (Standard)</option>
                        </select>
                    </div>
                    <button onclick="runPathTrace()" class="w-full py-2 px-4 rounded-lg bg-nvidia-green hover:bg-nvidia-lightGreen text-black font-bold text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-magnifying-glass-location"></i>
                        <span>Run NetQ Trace</span>
                    </button>
                </div>

                <!-- Trace Results Visualizer -->
                <div id="trace-result-container" class="bg-nvidia-black/90 border border-nvidia-border rounded-xl p-4 space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 text-xs font-mono border-b border-nvidia-border/70 pb-3">
                        <div class="text-slate-300">
                            Command: <span id="trace-cmd-text" class="text-nvidia-green">netq trace gpu-node-01 to gpu-node-08 vrf vrf-ai-train mtu 9000</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="px-2 py-0.5 rounded bg-nvidia-green/15 text-nvidia-green">ECMP Paths: 4 Valid</span>
                            <span id="trace-total-latency" class="px-2 py-0.5 rounded bg-blue-500/15 text-blue-400">Total RTT: 2.14 µs</span>
                        </div>
                    </div>

                    <!-- Hop-by-Hop Flow Diagram -->
                    <div id="trace-hops-visual" class="grid grid-cols-1 md:grid-cols-5 gap-3 items-center">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>

            <!-- Bottom Section: Fabric Validation Suite (netq check) -->
            <div class="bg-nvidia-card border border-nvidia-border rounded-xl overflow-hidden">
                <div class="px-5 py-4 border-b border-nvidia-border flex flex-wrap items-center justify-between gap-3 bg-nvidia-surface/50">
                    <div>
                        <h3 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-list-check text-nvidia-green"></i>
                            Fabric-Wide Health & Consistency Validation (<code class="text-nvidia-green text-sm">netq check</code>)
                        </h3>
                        <p class="text-xs text-nvidia-muted">Automated state verification across control-plane and data-plane protocols</p>
                    </div>
                    <button onclick="runAllNetqChecks()" id="run-checks-btn" class="px-4 py-2 rounded-lg bg-nvidia-black hover:bg-nvidia-border border border-nvidia-green/50 text-nvidia-green text-xs font-semibold transition flex items-center gap-2">
                        <i class="fa-solid fa-rotate"></i>
                        <span>Run Full Fabric Validation</span>
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-5" id="netq-checks-grid">
                    <!-- Populated by JS -->
                </div>
            </div>
        </section>

        <!-- ===================================================================== -->
        <!-- TAB 4: ARCHITECTURE & CLI REFERENCE                                   -->
        <!-- ===================================================================== -->
        <section id="panel-reference" class="tab-panel hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Architecture Overview (6 Columns) -->
                <div class="lg:col-span-6 bg-nvidia-card border border-nvidia-border rounded-xl p-5 space-y-4">
                    <h2 class="text-base font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-layer-group text-nvidia-green"></i>
                        NVIDIA NetQ Telemetry & Automation Architecture
                    </h2>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        NVIDIA NetQ is a highly scalable network operations toolset that provides real-time visibility, troubleshooting, and lifecycle validation for Cumulus Linux, SONiC, and BlueField DPU fabrics.
                    </p>

                    <div class="space-y-3">
                        <div class="p-3.5 rounded-lg bg-nvidia-black border border-nvidia-border">
                            <h4 class="text-xs font-bold text-nvidia-green uppercase font-mono">1. Streaming Telemetry Agent (netq-agent)</h4>
                            <p class="text-xs text-slate-400 mt-1">
                                Runs natively on Spectrum switches and DGX hosts. Streams kernel netlink events, BGP/EVPN state, RoCEv2 ECN/PFC counters, and ASIC buffer telemetry via OpenTelemetry / gRPC without polling overhead.
                            </p>
                        </div>
                        <div class="p-3.5 rounded-lg bg-nvidia-black border border-nvidia-border">
                            <h4 class="text-xs font-bold text-nvidia-green uppercase font-mono">2. Time-Series & Graph Analytics Engine</h4>
                            <p class="text-xs text-slate-400 mt-1">
                                Stores historical fabric state, enabling <strong>"What Just Happened" (WJH)</strong> hardware packet drop root-cause analysis and point-in-time fabric state comparison.
                            </p>
                        </div>
                        <div class="p-3.5 rounded-lg bg-nvidia-black border border-nvidia-border">
                            <h4 class="text-xs font-bold text-nvidia-green uppercase font-mono">3. Closed-Loop CI/CD & ZTP Integration</h4>
                            <p class="text-xs text-slate-400 mt-1">
                                Integrates with Ansible, GitLab/GitHub Actions, and NVUE (NVIDIA User Experience) declarative YAML APIs to validate every configuration change prior to production commit.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Interactive NetQ & NVUE CLI Cheat Sheet (6 Columns) -->
                <div class="lg:col-span-6 bg-nvidia-card border border-nvidia-border rounded-xl p-5 space-y-4">
                    <div class="flex items-center justify-between">
                        <h2 class="text-base font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-terminal text-nvidia-green"></i>
                            Essential NetQ & NVUE CLI Reference
                        </h2>
                        <span class="text-[11px] font-mono text-nvidia-muted">Click any command to copy</span>
                    </div>

                    <div class="space-y-2.5" id="cli-reference-list">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="border-t border-nvidia-border bg-nvidia-surface/60 py-4 px-6 mt-auto">
        <div class="max-w-[1600px] mx-auto flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-nvidia-muted">
            <div>
                NVIDIA NetQ Network Telemetry & Automation Simulation Portal • <span class="text-slate-300 font-mono">Spectrum-X AI Ethernet Reference</span>
            </div>
            <div class="font-mono text-[11px]">
                Telemetry Engine: <span class="text-nvidia-green">ACTIVE</span> • NVUE API: <span class="text-nvidia-green">v2.1</span>
            </div>
        </div>
    </footer>

    <!-- ===================================================================== -->
    <!-- JAVASCRIPT APPLICATION LOGIC                                          -->
    <!-- ===================================================================== -->
    <script>
        // -------------------------------------------------------------------------
        // 1. STATE & FABRIC DATA MODEL
        // -------------------------------------------------------------------------
        const fabricNodes = [
            // Super-Spines
            { id: 'sspine-01', name: 'sspine-01', tier: 'superspine', x: 280, y: 45, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 44.1, util: 52.3, ports: '64 / 64 UP', buffer: 14.2, ip: '10.255.0.1/32' },
            { id: 'sspine-02', name: 'sspine-02', tier: 'superspine', x: 520, y: 45, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 44.8, util: 51.9, ports: '64 / 64 UP', buffer: 13.8, ip: '10.255.0.2/32' },
            // Spines
            { id: 'spine-01', name: 'spine-01', tier: 'spine', x: 180, y: 150, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 47.0, util: 64.5, ports: '64 / 64 UP', buffer: 19.1, ip: '10.255.0.3/32' },
            { id: 'spine-02', name: 'spine-02', tier: 'spine', x: 330, y: 150, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 46.5, util: 63.8, ports: '64 / 64 UP', buffer: 18.4, ip: '10.255.0.4/32' },
            { id: 'spine-03', name: 'spine-03', tier: 'spine', x: 480, y: 150, status: 'warning', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 58.4, util: 84.2, ports: '63 / 64 UP', buffer: 41.0, ip: '10.255.0.5/32' },
            { id: 'spine-04', name: 'spine-04', tier: 'spine', x: 630, y: 150, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 47.2, util: 62.9, ports: '64 / 64 UP', buffer: 17.9, ip: '10.255.0.6/32' },
            // Leafs
            { id: 'leaf-01', name: 'leaf-01', tier: 'leaf', x: 140, y: 260, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 46.2, util: 68.4, ports: '62 / 64 UP', buffer: 18.5, ip: '10.255.0.11/32' },
            { id: 'leaf-02', name: 'leaf-02', tier: 'leaf', x: 245, y: 260, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 45.9, util: 66.1, ports: '64 / 64 UP', buffer: 16.2, ip: '10.255.0.12/32' },
            { id: 'leaf-03', name: 'leaf-03', tier: 'leaf', x: 350, y: 260, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'SONiC 202311', temp: 48.1, util: 71.0, ports: '64 / 64 UP', buffer: 22.0, ip: '10.255.0.13/32' },
            { id: 'leaf-04', name: 'leaf-04', tier: 'leaf', x: 455, y: 260, status: 'degraded', model: 'NVIDIA Spectrum-4 SN5600', os: 'SONiC 202311', temp: 61.5, util: 79.4, ports: '61 / 64 UP', buffer: 48.7, ip: '10.255.0.14/32' },
            { id: 'leaf-05', name: 'leaf-05', tier: 'leaf', x: 560, y: 260, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 45.3, util: 65.0, ports: '64 / 64 UP', buffer: 15.8, ip: '10.255.0.15/32' },
            { id: 'leaf-06', name: 'leaf-06', tier: 'leaf', x: 665, y: 260, status: 'healthy', model: 'NVIDIA Spectrum-4 SN5600', os: 'Cumulus Linux 5.9.1', temp: 46.7, util: 67.8, ports: '64 / 64 UP', buffer: 17.4, ip: '10.255.0.16/32' },
            // DGX H100 Compute Hosts
            { id: 'gpu-01', name: 'DGX-01', tier: 'host', x: 192, y: 370, status: 'healthy', model: 'NVIDIA DGX H100 (8x ConnectX-7)', os: 'Ubuntu 22.04 + DOCA 2.6', temp: 51.0, util: 88.0, ports: '8x 400GbE UP', buffer: 12.0, ip: '10.10.10.11/24' },
            { id: 'gpu-02', name: 'DGX-02', tier: 'host', x: 402, y: 370, status: 'healthy', model: 'NVIDIA DGX H100 (8x ConnectX-7)', os: 'Ubuntu 22.04 + DOCA 2.6', temp: 52.4, util: 91.2, ports: '8x 400GbE UP', buffer: 14.5, ip: '10.10.20.14/24' },
            { id: 'gpu-03', name: 'DGX-03', tier: 'host', x: 612, y: 370, status: 'healthy', model: 'NVIDIA DGX H100 (8x ConnectX-7)', os: 'Ubuntu 22.04 + DOCA 2.6', temp: 50.8, util: 86.5, ports: '8x 400GbE UP', buffer: 11.8, ip: '10.10.30.18/24' }
        ];

        // Generate Clos Links between Tiers
        const fabricLinks = [];
        const superSpines = fabricNodes.filter(n => n.tier === 'superspine');
        const spines = fabricNodes.filter(n => n.tier === 'spine');
        const leafs = fabricNodes.filter(n => n.tier === 'leaf');
        const hosts = fabricNodes.filter(n => n.tier === 'host');

        superSpines.forEach(ss => {
            spines.forEach(sp => fabricLinks.push({ source: ss, target: sp }));
        });
        spines.forEach(sp => {
            leafs.forEach(lf => fabricLinks.push({ source: sp, target: lf }));
        });
        // Dual-homed GPU pods to Leaf pairs (MLAG / EVPN Multihoming)
        fabricLinks.push({ source: leafs[0], target: hosts[0] }, { source: leafs[1], target: hosts[0] });
        fabricLinks.push({ source: leafs[2], target: hosts[1] }, { source: leafs[3], target: hosts[1] });
        fabricLinks.push({ source: leafs[4], target: hosts[2] }, { source: leafs[5], target: hosts[2] });

        let selectedNodeId = 'leaf-01';
        let isStreaming = true;
        let currentAlarmFilter = 'ALL';

        let alarmsData = [
            { id: 101, time: '22:19:42', severity: 'CRITICAL', node: 'leaf-04 (swp49)', message: 'Optical Transceiver Rx Power Low (-11.4 dBm) & CRC Errors detected on 800G uplink', status: 'OPEN' },
            { id: 102, time: '22:14:10', severity: 'WARNING', node: 'spine-03 (ASIC)', message: 'RoCEv2 ECN marking threshold exceeded (41% shared buffer occupancy) during AllReduce burst', status: 'OPEN' },
            { id: 103, time: '22:05:55', severity: 'WARNING', node: 'leaf-04 (swp12)', message: 'MTU mismatch warning on peer LLDP neighbor (Expected 9216, Received 9000)', status: 'OPEN' },
            { id: 104, time: '21:48:19', severity: 'INFO', node: 'leaf-01', message: 'NVUE configuration revision 42 committed cleanly; all 16 BGP EVPN peers verified', status: 'ACKED' },
            { id: 105, time: '21:30:04', severity: 'INFO', node: 'sspine-01', message: 'NetQ streaming telemetry agent heartbeat synced with collector cluster', status: 'ACKED' }
        ];

        // -------------------------------------------------------------------------
        // 2. TAB NAVIGATION & TOAST UTILITY
        // -------------------------------------------------------------------------
        function switchTab(tabName) {
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.add('hidden'));
            document.getElementById(`panel-${tabName}`).classList.remove('hidden');

            document.querySelectorAll('.nav-tab').forEach(btn => {
                btn.classList.remove('bg-nvidia-green', 'text-black', 'font-semibold', 'shadow');
                btn.classList.add('text-slate-400', 'hover:text-white', 'hover:bg-nvidia-card');
            });

            const activeBtn = document.getElementById(`tab-btn-${tabName}`);
            activeBtn.classList.remove('text-slate-400', 'hover:text-white', 'hover:bg-nvidia-card');
            activeBtn.classList.add('bg-nvidia-green', 'text-black', 'font-semibold', 'shadow');

            if (tabName === 'telemetry') {
                resizeTelemetryCanvas();
            }
        }

        function showToast(title, message, type = 'success') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            const borderCol = type === 'success' ? 'border-nvidia-green' : (type === 'warn' ? 'border-amber-400' : 'border-blue-400');
            const iconHtml = type === 'success'
                ? '<i class="fa-solid fa-circle-check text-nvidia-green text-base"></i>'
                : '<i class="fa-solid fa-circle-info text-amber-400 text-base"></i>';

            toast.className = `pointer-events-auto bg-nvidia-card/95 backdrop-blur border-l-4 ${borderCol} border border-nvidia-border rounded-lg p-3.5 shadow-2xl max-w-sm flex items-start gap-3 transition-all duration-300 transform translate-y-2 opacity-0`;
            toast.innerHTML = `
                <div class="mt-0.5">${iconHtml}</div>
                <div class="flex-1">
                    <div class="text-xs font-bold text-white">${title}</div>
                    <div class="text-[11px] text-slate-300 mt-0.5">${message}</div>
                </div>
            `;
            container.appendChild(toast);
            requestAnimationFrame(() => {
                toast.classList.remove('translate-y-2', 'opacity-0');
            });
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => toast.remove(), 300);
            }, 3500);
        }

        // -------------------------------------------------------------------------
        // 3. INTERACTIVE TOPOLOGY VISUALIZER & NODE INSPECTOR
        // -------------------------------------------------------------------------
        function renderTopology() {
            const linksGroup = document.getElementById('topo-links');
            const nodesGroup = document.getElementById('topo-nodes');
            linksGroup.innerHTML = '';
            nodesGroup.innerHTML = '';

            // Draw links
            fabricLinks.forEach((link, idx) => {
                const isConnectedToSelected = link.source.id === selectedNodeId || link.target.id === selectedNodeId;
                const isDegraded = link.source.status === 'degraded' || link.target.status === 'degraded';

                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', link.source.x);
                line.setAttribute('y1', link.source.y);
                line.setAttribute('x2', link.target.x);
                line.setAttribute('y2', link.target.y);
                line.setAttribute('stroke', isDegraded ? '#F43F5E' : (isConnectedToSelected ? '#76B900' : '#263241'));
                line.setAttribute('stroke-width', isConnectedToSelected ? '2.5' : '1.3');
                line.setAttribute('opacity', isConnectedToSelected ? '1' : '0.65');
                if (isConnectedToSelected) {
                    line.classList.add('topo-link-active');
                }
                linksGroup.appendChild(line);
            });

            // Draw nodes
            fabricNodes.forEach(node => {
                const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                g.setAttribute('transform', `translate(${node.x}, ${node.y})`);
                g.style.cursor = 'pointer';
                g.onclick = () => selectNode(node.id);

                const isSelected = node.id === selectedNodeId;
                const statusColor = node.status === 'healthy' ? '#76B900' : (node.status === 'warning' ? '#FBBF24' : '#F43F5E');

                // Selection highlight halo
                if (isSelected) {
                    const halo = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                    halo.setAttribute('x', -44);
                    halo.setAttribute('y', -22);
                    halo.setAttribute('width', 88);
                    halo.setAttribute('height', 44);
                    halo.setAttribute('rx', 10);
                    halo.setAttribute('fill', 'rgba(118, 185, 0, 0.14)');
                    halo.setAttribute('stroke', '#76B900');
                    halo.setAttribute('stroke-width', '2');
                    g.appendChild(halo);
                }

                // Node body box
                const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                rect.setAttribute('x', -38);
                rect.setAttribute('y', -16);
                rect.setAttribute('width', 76);
                rect.setAttribute('height', 32);
                rect.setAttribute('rx', 6);
                rect.setAttribute('fill', node.tier === 'host' ? '#131B26' : '#18212D');
                rect.setAttribute('stroke', isSelected ? '#76B900' : '#334155');
                rect.setAttribute('stroke-width', '1.5');
                g.appendChild(rect);

                // Status indicator dot
                const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                dot.setAttribute('cx', -26);
                dot.setAttribute('cy', 0);
                dot.setAttribute('r', 4);
                dot.setAttribute('fill', statusColor);
                g.appendChild(dot);

                // Node label
                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', -17);
                text.setAttribute('y', 4);
                text.setAttribute('fill', '#F8FAFC');
                text.setAttribute('font-size', '10.5');
                text.setAttribute('font-family', 'JetBrains Mono');
                text.setAttribute('font-weight', isSelected ? '700' : '500');
                text.textContent = node.name;
                g.appendChild(text);

                nodesGroup.appendChild(g);
            });
        }

        function selectNode(nodeId) {
            selectedNodeId = nodeId;
            const node = fabricNodes.find(n => n.id === nodeId);
            if (!node) return;

            document.getElementById('insp-name').textContent = node.name;
            document.getElementById('insp-model').textContent = `${node.model} • ${node.os}`;
            document.getElementById('insp-temp').textContent = `${node.temp.toFixed(1)} °C`;
            document.getElementById('insp-util').textContent = `${node.util.toFixed(1)}%`;
            document.getElementById('insp-ports').textContent = node.ports;
            document.getElementById('insp-buffer').textContent = `${node.buffer.toFixed(1)}%`;
            document.getElementById('insp-ip').textContent = `Loopback: ${node.ip}`;

            const badge = document.getElementById('insp-badge');
            badge.textContent = node.status.toUpperCase();
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase ' + (
                node.status === 'healthy' ? 'bg-nvidia-green/20 text-nvidia-green' :
                node.status === 'warning' ? 'bg-amber-500/20 text-amber-400' : 'bg-rose-500/20 text-rose-400'
            );

            // Render simulated port pills
            const pillsContainer = document.getElementById('insp-port-pills');
            pillsContainer.innerHTML = '';
            const samplePorts = ['swp1', 'swp2', 'swp3', 'swp4', 'swp49', 'swp50', 'swp51', 'swp52'];
            samplePorts.forEach((p, i) => {
                const isErr = (node.id === 'leaf-04' && p === 'swp49') || (node.id === 'spine-03' && p === 'swp51');
                const pill = document.createElement('span');
                pill.className = `px-2 py-0.5 rounded text-[10px] font-mono border ${
                    isErr ? 'bg-rose-500/15 border-rose-500/50 text-rose-400' : 'bg-nvidia-black border-nvidia-border text-slate-300'
                }`;
                pill.textContent = `${p}: ${isErr ? 'ERR' : '800G'}`;
                pillsContainer.appendChild(pill);
            });

            renderTopology();
        }

        // -------------------------------------------------------------------------
        // 4. REAL-TIME TELEMETRY CANVAS CHART
        // -------------------------------------------------------------------------
        const bwHistory = Array.from({ length: 36 }, (_, i) => 18.2 + Math.sin(i * 0.4) * 2.5 + Math.random() * 1.1);
        const bufHistory = Array.from({ length: 36 }, (_, i) => 22 + Math.cos(i * 0.35) * 6 + Math.random() * 3);

        function resizeTelemetryCanvas() {
            const canvas = document.getElementById('telemetry-chart');
            if (!canvas) return;
            const rect = canvas.parentElement.getBoundingClientRect();
            canvas.width = rect.width - 16;
            canvas.height = rect.height - 16;
            drawTelemetryChart();
        }

        function drawTelemetryChart() {
            const canvas = document.getElementById('telemetry-chart');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            if (w <= 0 || h <= 0) return;

            ctx.clearRect(0, 0, w, h);

            // Horizontal grid lines
            ctx.strokeStyle = '#1E293B';
            ctx.lineWidth = 1;
            for (let i = 1; i <= 3; i++) {
                const y = (h / 4) * i;
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(w, y);
                ctx.stroke();
            }

            // Helper to plot smooth line
            const plotSeries = (data, maxVal, strokeColor, fillGradientStart) => {
                const stepX = w / (data.length - 1);
                ctx.beginPath();
                data.forEach((val, idx) => {
                    const x = idx * stepX;
                    const y = h - (val / maxVal) * (h - 16) - 8;
                    if (idx === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                });
                ctx.strokeStyle = strokeColor;
                ctx.lineWidth = 2;
                ctx.stroke();

                if (fillGradientStart) {
                    ctx.lineTo(w, h);
                    ctx.lineTo(0, h);
                    ctx.closePath();
                    const grad = ctx.createLinearGradient(0, 0, 0, h);
                    grad.addColorStop(0, fillGradientStart);
                    grad.addColorStop(1, 'rgba(118, 185, 0, 0)');
                    ctx.fillStyle = grad;
                    ctx.fill();
                }
            };

            // Plot Bandwidth (max 25.6 Tbps)
            plotSeries(bwHistory, 25.6, '#76B900', 'rgba(118, 185, 0, 0.25)');
            // Plot Buffer Occupancy (max 100%)
            plotSeries(bufHistory, 100, '#22D3EE', null);

            // Current telemetry readout overlay
            const latestBw = bwHistory[bwHistory.length - 1].toFixed(2);
            const latestBuf = bufHistory[bufHistory.length - 1].toFixed(1);
            ctx.fillStyle = '#94A3B8';
            ctx.font = '10px JetBrains Mono';
            ctx.fillText(`Peak East-West: ${latestBw} Tbps | Avg Buffer: ${latestBuf}%`, 8, 13);
        }

        function tickTelemetryStream() {
            if (!isStreaming) return;

            // Push new telemetry samples
            const nextBw = Math.max(12, Math.min(24.8, bwHistory[bwHistory.length - 1] + (Math.random() - 0.48) * 1.4));
            const nextBuf = Math.max(10, Math.min(65, bufHistory[bufHistory.length - 1] + (Math.random() - 0.5) * 4.2));
            bwHistory.shift();
            bwHistory.push(nextBw);
            bufHistory.shift();
            bufHistory.push(nextBuf);

            // Slightly jitter selected node metrics
            const activeNode = fabricNodes.find(n => n.id === selectedNodeId);
            if (activeNode) {
                activeNode.util = Math.max(30, Math.min(96, activeNode.util + (Math.random() - 0.5) * 1.2));
                activeNode.temp = Math.max(40, Math.min(66, activeNode.temp + (Math.random() - 0.5) * 0.3));
                document.getElementById('insp-util').textContent = `${activeNode.util.toFixed(1)}%`;
                document.getElementById('insp-temp').textContent = `${activeNode.temp.toFixed(1)} °C`;
            }

            drawTelemetryChart();
        }

        function toggleStream() {
            isStreaming = !isStreaming;
            const icon = document.getElementById('stream-icon');
            const label = document.getElementById('stream-label');
            if (isStreaming) {
                icon.className = 'fa-solid fa-pause text-nvidia-green';
                label.textContent = 'Live';
                showToast('Telemetry Stream Resumed', 'Receiving 100ms gRPC/OTel updates from 12 switches.');
            } else {
                icon.className = 'fa-solid fa-play text-amber-400';
                label.textContent = 'Paused';
            }
        }

        // -------------------------------------------------------------------------
        // 5. ALARMS & REMEDIATION TABLE
        // -------------------------------------------------------------------------
        function renderAlarms() {
            const tbody = document.getElementById('alarms-tbody');
            tbody.innerHTML = '';

            const filtered = alarmsData.filter(a => currentAlarmFilter === 'ALL' || a.severity === currentAlarmFilter);

            filtered.forEach(alarm => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-nvidia-surface/60 transition';

                const sevBadge = alarm.severity === 'CRITICAL'
                    ? '<span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">CRITICAL</span>'
                    : alarm.severity === 'WARNING'
                    ? '<span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">WARNING</span>'
                    : '<span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30">INFO</span>';

                const actionBtn = alarm.status === 'OPEN'
                    ? `<button onclick="remediateAlarm(${alarm.id})" class="px-2.5 py-1 rounded bg-nvidia-green/15 hover:bg-nvidia-green hover:text-black text-nvidia-green border border-nvidia-green/40 text-[11px] font-semibold transition">Remediate</button>`
                    : `<span class="text-[11px] font-mono text-slate-500"><i class="fa-solid fa-check mr-1 text-nvidia-green"></i>Resolved</span>`;

                tr.innerHTML = `
                    <td class="py-3 px-4 font-mono text-slate-400 whitespace-nowrap">${alarm.time}</td>
                    <td class="py-3 px-4 whitespace-nowrap">${sevBadge}</td>
                    <td class="py-3 px-4 font-mono text-white whitespace-nowrap">${alarm.node}</td>
                    <td class="py-3 px-4 text-slate-300">${alarm.message}</td>
                    <td class="py-3 px-4 text-right whitespace-nowrap">${actionBtn}</td>
                `;
                tbody.appendChild(tr);
            });

            const openCount = alarmsData.filter(a => a.status === 'OPEN').length;
            document.getElementById('kpi-alerts-count').textContent = openCount;
        }

        function filterAlarms(severity) {
            currentAlarmFilter = severity;
            document.querySelectorAll('.alarm-filter-btn').forEach(btn => {
                if (btn.dataset.filter === severity) {
                    btn.className = 'alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-green text-black font-semibold';
                } else {
                    btn.className = 'alarm-filter-btn px-2.5 py-1 rounded-md text-xs font-medium bg-nvidia-black text-slate-300 border border-nvidia-border hover:border-slate-500';
                }
            });
            renderAlarms();
        }

        function remediateAlarm(id) {
            const alarm = alarmsData.find(a => a.id === id);
            if (!alarm) return;
            alarm.status = 'ACKED';

            // Heal corresponding node in topology if applicable
            if (alarm.node.includes('leaf-04')) {
                const n = fabricNodes.find(x => x.id === 'leaf-04');
                if (n) { n.status = 'healthy'; n.ports = '64 / 64 UP'; n.buffer = 19.2; }
            }
            if (alarm.node.includes('spine-03')) {
                const n = fabricNodes.find(x => x.id === 'spine-03');
                if (n) { n.status = 'healthy'; n.buffer = 21.0; }
            }

            renderAlarms();
            renderTopology();
            selectNode(selectedNodeId);
            showToast('Automated Remediation Executed', `NetQ playbook cleared anomaly on ${alarm.node}.`);
        }

        // -------------------------------------------------------------------------
        // 6. ZTP & CI/CD DEPLOYMENT AUTOMATION SIMULATOR
        // -------------------------------------------------------------------------
        const playbooks = {
            evpn: (targets) => `# NVUE Declarative Fabric Config + NetQ Pre/Post Validation
# Target Nodes: ${targets.join(', ')}
- set:
    router:
      bgp:
        autonomous-system: 65101
        enable: on
      vrf:
        default:
          router:
            bgp:
              address-family:
                l2vpn-evpn:
                  enable: on
              neighbor:
                swp49-52:
                  type: unnumbered
                  address-family:
                    l2vpn-evpn:
                      enable: on
    evpn:
      enable: on
      vni:
        10010:
          vrf: vrf-ai-train
# NetQ Post-Deployment Gate:
# $ netq check bgp && netq check evpn && netq check vxlan`,

            rocev2: (targets) => `# Spectrum-X RoCEv2 Lossless QoS & ECN Marking Profile
# Target Nodes: ${targets.join(', ')}
- set:
    qos:
      roce:
        enable: on
        mode: lossless
      ecn:
        traffic-class-3:
          min-threshold: 150KB
          max-threshold: 1500KB
          probability: 100
      pfc:
        profile-ai-fabric:
          tx: on
          rx: on
          priority-3: on
    interface:
      swp1-64:
        qos:
          pfc: profile-ai-fabric
# NetQ Post-Deployment Gate:
# $ netq check roce && netq check mtu`,

            ztp: (targets) => `# Zero-Touch Provisioning (ZTP) & Cumulus Linux 5.9 Rollout
# Target Nodes: ${targets.join(', ')}
ztp_workflow:
  dhcp_option_239: "http://netq-ztp.local/scripts/cumulus-ztp.sh"
  os_image: "cumulus-linux-5.9.1-mlx-amd64.bin"
  install_netq_agent: true
  telemetry_server: "10.255.100.10:32767"
  post_boot_checks:
    - "netq show agents"
    - "netq check interfaces"
    - "netq check ntp"`
        };

        function getSelectedTargets() {
            const checks = document.querySelectorAll('#target-switches-grid input[type="checkbox"]:checked');
            const vals = Array.from(checks).map(c => c.value);
            return vals.length > 0 ? vals : ['leaf-01'];
        }

        function updatePlaybookPreview() {
            const type = document.getElementById('playbook-select').value;
            const targets = getSelectedTargets();
            document.getElementById('yaml-preview').textContent = playbooks[type](targets);
        }

        function copyPlaybookCode() {
            const text = document.getElementById('yaml-preview').textContent;
            const textarea = document.createElement('textarea');
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            showToast('YAML Copied', 'NVUE configuration manifest copied to clipboard.');
        }

        function clearPipelineLogs() {
            document.getElementById('pipeline-console').innerHTML = '<div class="text-slate-500"># Console cleared. Ready for next deployment run...</div>';
        }

        let pipelineRunning = false;
        function runDeploymentPipeline() {
            if (pipelineRunning) return;
            pipelineRunning = true;

            const targets = getSelectedTargets();
            const playbookName = document.getElementById('playbook-select').options[document.getElementById('playbook-select').selectedIndex].text;
            const btn = document.getElementById('run-pipeline-btn');
            const badge = document.getElementById('pipeline-status-badge');
            const consoleEl = document.getElementById('pipeline-console');

            btn.disabled = true;
            btn.classList.add('opacity-60', 'cursor-not-allowed');
            badge.textContent = 'RUNNING...';
            badge.className = 'px-2.5 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-400';

            // Reset stages
            for (let i = 1; i <= 5; i++) {
                const st = document.getElementById(`stage-${i}`);
                st.className = 'pipeline-stage p-3 rounded-lg bg-nvidia-black border border-nvidia-border text-center transition-all';
                st.querySelector('.stage-sub').textContent = 'Pending';
                st.querySelector('.stage-sub').className = 'text-[10px] font-mono text-slate-500 mt-0.5 stage-sub';
            }

            consoleEl.innerHTML = '';
            const log = (msg, colorClass = 'text-slate-300') => {
                const line = document.createElement('div');
                const ts = new Date().toTimeString().split(' ')[0];
                line.className = colorClass;
                line.innerHTML = `<span class="text-slate-500">[${ts}]</span> ${msg}`;
                consoleEl.appendChild(line);
                consoleEl.scrollTop = consoleEl.scrollHeight;
            };

            const steps = [
                {
                    stage: 1,
                    delay: 400,
                    fn: () => {
                        log(`Triggering GitOps pipeline for playbook: <strong class="text-white">${playbookName}</strong>`, 'text-cyan-400');
                        log(`Target inventory (${targets.length} nodes): ${targets.join(', ')}`);
                    }
                },
                {
                    stage: 2,
                    delay: 1400,
                    fn: () => {
                        log(`Running NetQ baseline snapshot: <code class="text-nvidia-green">netq check bgp && netq check evpn</code>`);
                        log(`Baseline check PASSED: 0 critical anomalies detected prior to change.`, 'text-nvidia-green');
                    }
                },
                {
                    stage: 3,
                    delay: 2500,
                    fn: () => {
                        log(`Applying declarative NVUE configuration via REST API (nv config apply)...`, 'text-amber-300');
                        targets.forEach(t => log(`  -> ${t}: NVUE revision staged & applied (0.42s)`));
                    }
                },
                {
                    stage: 4,
                    delay: 3700,
                    fn: () => {
                        log(`Executing NetQ post-deployment validation suite...`);
                        log(`  [PASS] BGP Unnumbered neighbors established on ${targets.join(', ')}`, 'text-nvidia-green');
                        log(`  [PASS] VXLAN VNI 10010 & RoCEv2 ECN queues verified lossless`, 'text-nvidia-green');
                    }
                },
                {
                    stage: 5,
                    delay: 4700,
                    fn: () => {
                        log(`All NetQ validation gates passed! Saving NVUE startup config (nv config save).`, 'text-nvidia-green font-bold');
                        badge.textContent = 'SUCCEEDED';
                        badge.className = 'px-2.5 py-0.5 rounded text-[11px] font-mono bg-nvidia-green/20 text-nvidia-green font-bold';
                        btn.disabled = false;
                        btn.classList.remove('opacity-60', 'cursor-not-allowed');
                        pipelineRunning = false;
                        showToast('Deployment Pipeline Succeeded', `Verified & committed configuration across ${targets.length} nodes.`);
                    }
                }
            ];

            steps.forEach((step, idx) => {
                setTimeout(() => {
                    // Mark previous stage complete
                    if (idx > 0) {
                        const prev = document.getElementById(`stage-${idx}`);
                        prev.classList.remove('border-amber-400');
                        prev.classList.add('border-nvidia-green', 'bg-nvidia-green/10');
                        prev.querySelector('.stage-sub').textContent = 'Passed';
                        prev.querySelector('.stage-sub').className = 'text-[10px] font-mono text-nvidia-green mt-0.5 stage-sub';
                    }

                    const curr = document.getElementById(`stage-${step.stage}`);
                    curr.classList.add('border-amber-400');
                    curr.querySelector('.stage-sub').textContent = 'Running...';
                    curr.querySelector('.stage-sub').className = 'text-[10px] font-mono text-amber-400 mt-0.5 stage-sub';

                    step.fn();

                    if (step.stage === 5) {
                        curr.classList.remove('border-amber-400');
                        curr.classList.add('border-nvidia-green', 'bg-nvidia-green/10');
                        curr.querySelector('.stage-sub').textContent = 'Committed';
                        curr.querySelector('.stage-sub').className = 'text-[10px] font-mono text-nvidia-green mt-0.5 stage-sub';
                    }
                }, step.delay);
            });
        }

        // -------------------------------------------------------------------------
        // 7. TRACE & VALIDATION ENGINE (netq trace & netq check)
        // -------------------------------------------------------------------------
        function runPathTrace() {
            const src = document.getElementById('trace-src').value;
            const dst = document.getElementById('trace-dst').value;
            const vrf = document.getElementById('trace-vrf').value;
            const mtu = document.getElementById('trace-mtu').value;

            document.getElementById('trace-cmd-text').textContent = `netq trace ${src} to ${dst} vrf ${vrf.split(' ')[0]} mtu ${mtu}`;

            const hops = [
                { node: src, role: 'Source DGX H100', encap: `Inner IPv4 / RoCEv2 (MTU ${mtu})`, latency: '0.00 µs', status: 'OK' },
                { node: 'leaf-01', role: 'Ingress VTEP (10.255.0.11)', encap: 'VXLAN Encap VNI 10010 (UDP 4789)', latency: '0.52 µs', status: 'OK' },
                { node: 'spine-02', role: 'Underlay ECMP Transit', encap: 'Outer IPv4 / BGP Unnumbered', latency: '1.08 µs', status: 'OK' },
                { node: 'leaf-05', role: 'Egress VTEP (10.255.0.15)', encap: 'VXLAN Decap -> VLAN 10', latency: '1.62 µs', status: 'OK' },
                { node: dst, role: 'Destination DGX H100', encap: `Delivered (0 Drops / MTU ${mtu} Verified)`, latency: '2.14 µs', status: 'OK' }
            ];

            const container = document.getElementById('trace-hops-visual');
            container.innerHTML = '';

            hops.forEach((h, i) => {
                const card = document.createElement('div');
                card.className = 'bg-nvidia-card border border-nvidia-green/40 rounded-lg p-3 relative';
                card.innerHTML = `
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-nvidia-green/15 text-nvidia-green font-bold">HOP ${i + 1}</span>
                        <span class="text-[11px] font-mono text-cyan-400">${h.latency}</span>
                    </div>
                    <div class="text-xs font-bold font-mono text-white">${h.node}</div>
                    <div class="text-[11px] text-slate-400 mt-0.5">${h.role}</div>
                    <div class="mt-2 pt-2 border-t border-nvidia-border text-[10px] font-mono text-slate-300">${h.encap}</div>
                `;
                container.appendChild(card);
            });

            showToast('NetQ Path Trace Complete', `Verified VXLAN overlay & underlay path from ${src} to ${dst}.`);
        }

        const netqCheckItems = [
            { name: 'BGP Unnumbered Sessions', cmd: 'netq check bgp', status: 'PASS', summary: '64/64 IPv4 & L2VPN EVPN sessions Established', tip: 'All spine-leaf peerings healthy.' },
            { name: 'EVPN Type-2 / Type-5 Routes', cmd: 'netq check evpn', status: 'PASS', summary: '1,248 MAC/IP & Host routes synchronized across VTEPs', tip: 'Zero duplicate MAC mobility events.' },
            { name: 'VXLAN Tunnel & VNI Consistency', cmd: 'netq check vxlan', status: 'PASS', summary: 'All 6 VTEPs mapped consistently to VNI 10010 & 10020', tip: 'Anycast VTEP VIPs verified.' },
            { name: 'End-to-End Jumbo MTU (9216)', cmd: 'netq check mtu', status: 'WARN', summary: '1 interface mismatch detected on leaf-04:swp12 (9000 vs 9216)', tip: 'Run NVUE set interface swp12 link mtu 9216.' },
            { name: 'RoCEv2 Lossless QoS & ECN', cmd: 'netq check roce', status: 'PASS', summary: 'PFC priority-3 & WRED/ECN thresholds uniform across fabric', tip: 'Zero PFC watchdog triggers.' },
            { name: 'PTP / NTP Clock Synchronization', cmd: 'netq check ntp', status: 'PASS', summary: 'All 12 switches & 3 DGX pods within < 120ns offset', tip: 'Stratum-1 GPS grandmaster locked.' }
        ];

        function renderNetqChecks() {
            const grid = document.getElementById('netq-checks-grid');
            grid.innerHTML = '';

            netqCheckItems.forEach(item => {
                const isPass = item.status === 'PASS';
                const card = document.createElement('div');
                card.className = `p-4 rounded-xl bg-nvidia-black border ${isPass ? 'border-nvidia-border' : 'border-amber-500/50'} space-y-2`;
                card.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-white">${item.name}</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold ${isPass ? 'bg-nvidia-green/20 text-nvidia-green' : 'bg-amber-500/20 text-amber-400'}">
                            ${item.status}
                        </span>
                    </div>
                    <div class="text-[11px] font-mono text-cyan-400">$ ${item.cmd}</div>
                    <p class="text-xs text-slate-300">${item.summary}</p>
                    <p class="text-[11px] text-slate-500 italic">${item.tip}</p>
                `;
                grid.appendChild(card);
            });
        }

        function runAllNetqChecks() {
            const btn = document.getElementById('run-checks-btn');
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i><span>Validating Fabric...</span>';
            setTimeout(() => {
                renderNetqChecks();
                btn.innerHTML = '<i class="fa-solid fa-rotate"></i><span>Run Full Fabric Validation</span>';
                showToast('Fabric Validation Finished', 'Completed 6 protocol & hardware consistency suites.');
            }, 650);
        }

        // -------------------------------------------------------------------------
        // 8. CLI REFERENCE DATA
        // -------------------------------------------------------------------------
        const cliCommands = [
            { cmd: 'netq show events severity critical', desc: 'List real-time critical hardware, link, and protocol anomalies' },
            { cmd: 'netq check bgp include spine-01 leaf-01', desc: 'Verify BGP Unnumbered & EVPN peering consistency across nodes' },
            { cmd: 'netq trace gpu-node-01 to gpu-node-08 vrf vrf-ai-train', desc: 'Trace VXLAN overlay & ECMP underlay forwarding path' },
            { cmd: 'netq show drops reason buffer-congestion', desc: 'Inspect Spectrum ASIC "What Just Happened" (WJH) packet drops' },
            { cmd: 'nv config patch fabric-evpn.yaml && nv config apply', desc: 'Apply declarative NVUE YAML configuration atomically' },
            { cmd: 'netq show agents', desc: 'Verify telemetry agent health and streaming latency across pods' }
        ];

        function renderCliReference() {
            const list = document.getElementById('cli-reference-list');
            list.innerHTML = '';
            cliCommands.forEach(item => {
                const row = document.createElement('div');
                row.className = 'p-3 rounded-lg bg-nvidia-black border border-nvidia-border hover:border-nvidia-green/60 cursor-pointer transition group';
                row.onclick = () => {
                    const ta = document.createElement('textarea');
                    ta.value = item.cmd;
                    document.body.appendChild(ta);
                    ta.select();
                    document.execCommand('copy');
                    document.body.removeChild(ta);
                    showToast('Command Copied', item.cmd);
                };
                row.innerHTML = `
                    <div class="flex items-center justify-between">
                        <code class="text-xs font-mono text-nvidia-green font-semibold">${item.cmd}</code>
                        <i class="fa-regular fa-copy text-slate-500 group-hover:text-white text-xs"></i>
                    </div>
                    <p class="text-[11px] text-slate-400 mt-1">${item.desc}</p>
                `;
                list.appendChild(row);
            });
        }

        // -------------------------------------------------------------------------
        // 9. INITIALIZATION ON WINDOW LOAD
        // -------------------------------------------------------------------------
        window.addEventListener('load', () => {
            renderTopology();
            selectNode('leaf-01');
            renderAlarms();
            updatePlaybookPreview();
            runPathTrace();
            renderNetqChecks();
            renderCliReference();
            resizeTelemetryCanvas();

            window.addEventListener('resize', resizeTelemetryCanvas);
            setInterval(tickTelemetryStream, 1500);
        });
    </script>
</body>
</html>
