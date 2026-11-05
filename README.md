# Sauti Tri-Sense: Community-Led Early Warning for Population & Workforce Health

### Future Health Challenge 2026 – To Sense is to Predict | Track: Population and Workforce Health Early Warning

> **Tagline:** To Sense is to Predict – Listen to Community, Sense Water, Protect Health.

**Team Lead:** Abdulkadir Ahmed – FCT Abuja, Nigeria | 【entity-GitHub¦canonical_name=GitHub】: @abdulahmed1127-cyber | Email: aabdulkadir222@gmail.com
**Primary Challenge:** [Population Health] Population and Workforce Health Early Warning
**Tech Types:** AI agent, Machine learning, Software application, Analytics, Sensor, Connected device

#### Links
- GitHub: https://github.com/abdulahmed1127-cyber/Sauti-Tri-Sense
- Prototype Link: https://github.com/abdulahmed1127-cyber/Sauti-Tri-Sense
- Live Demo: https://lovable.dev/projects/sauti-tri-sense-demo
- Solution Deck: docs/Sauti_Tri_Sense_Solution_Deck.pdf

#### Problem
Nigeria's early warning is reactive. Facility-based IDSR reports outbreaks 2-3 weeks late. 40% rural water points have intermittent chemical contamination (fluoride, heavy metals) untested. Informal workforce faces chemical/heat risks with no sensing.

#### Solution – 3 Modules
1. **Sauti Community:** 30-sec Hausa/English voice report via offline-first Android app → On-device Whisper-Hausa STT → LLM symptom extraction → Anomaly detection (Isolation Forest, 5x baseline) → LGA Dashboard alert + SMS.
2. **Sauti ChemSafe:** $0.20 strip + phone camera colorimetric reader (OpenCV) → pH/conductivity vs WHO limit → hotspot map + safe-water advisory – closes screening-to-care loop.
3. **Sauti Wellbeing:** Hausa voice chatbot sustains handwashing, tracks referral completion to PHC, screens PHQ-2, escalates.

#### Quick Start
Backend:
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Mobile App:
cd mobile-app
npm install
npx expo start

#### Impact – Abuja Pilot (Abaji)
10 wards, 50 volunteers, 6 months: Detect 7-14 days earlier, reduce water-borne cases 25%, increase referral completion 30%→65%, reach 10k households. Scalable to ECOWAS.

#### Responsible AI
On-device processing, consent-based, federated learning, explainable alerts.

#### License
MIT – For Future Health Challenge 2026 – To Sense is to Predict
