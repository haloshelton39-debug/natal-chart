(function(){
    // Safety: wait until DOM is ready
    function onReady(fn){
        if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
        else fn();
    }

    function safeGet(id){ return document.getElementById(id); }

    // Practical suggestions for planets (short, 1-3 actionable steps)
    function getWorkSuggestionsForPlanet(planetName, signIndex, houseNumber){
        const p = planetName.toLowerCase();
        const suggestions = {
            sun: [
                'Укрепляйте уверенность через небольшие публичные выступления или ведение дневника достижений.',
                'Развивайте творческую практику: рисуйте, пишите или занимайтесь актёрской импровизацией.'
            ],
            moon: [
                'Ведите эмоциональный дневник и отслеживайте реакции в течение недели.',
                'Практикуйте заботу о себе: ритуалы сна, тёплые ванны, спокойные вечерние процедуры.'
            ],
            mercury: [
                'Поставьте себе маленькую цель по улучшению навыка общения: курс, подкаст или публичное выступление.',
                'Делайте запись мыслей голосом — это помогает структурировать идеи.'
            ],
            venus: [
                'Работайте над отношениями через честные разговоры и маленькие проявления внимания.',
                'Развивайте эстетическое хобби: украшение интерьера, музыка, мода.'
            ],
            mars: [
                'Направьте энергию в регулярные физические нагрузки или боевые искусства.',
                'Учитесь управлять импульсами: практика пауз перед действием (5–10 секунд).'
            ],
            jupiter: [
                'Расширяйтесь через изучение новых дисциплин и участие в групповых проектах.',
                'Запланируйте действие, которое кажется «чуть больше» привычного — путешествие или мастер-класс.'
            ],
            saturn: [
                'Установите чёткие цели и маленькие сроки — дисциплина укрепляет результат.',
                'Работайте с наставником или создайте систему ответственности (еженедельные отчёты).'
            ],
            uranus: [
                'Включайте эксперименты в рутину: новые техники работы, альтернативные маршруты.',
                'Поддерживайте связь с технологичными/околопрогрессивными сообществами.'
            ],
            neptune: [
                'Практики визуализации и мечты: ведите «карту желаний» и медитации на вдохновение.',
                'Будьте внимательны к границам — учитесь отличать вдохновение от иллюзий.'
            ],
            pluto: [
                'Работайте с психотерапевтом или пишите автобиографию — трансформация через рассказ о себе.',
                'Пробуйте ритуалы отпускания: запись, сожжение метафорических «письем-обид». '
            ]
        };

        const list = suggestions[p] || ['Наблюдайте, фиксируйте и делайте маленькие шаги в направлении изменений.'];
        // При наличии дома — попытка уточнить практику
        if(houseNumber){
            list[0] = (houseNumber === 1) ? (list[0] + ' Начните с небольших изменений в самопрезентации.') : list[0];
        }
        return list;
    }

    function getWorkSuggestionsForAspect(aspect){
        const name = aspect.name || '';
        const planet1 = (window.PLANETS_RU && PLANETS_RU[aspect.planet1]) ? PLANETS_RU[aspect.planet1] : aspect.planet1;
        const planet2 = (window.PLANETS_RU && PLANETS_RU[aspect.planet2]) ? PLANETS_RU[aspect.planet2] : aspect.planet2;
        const base = [];
        if(name === 'Соединение'){
            base.push(`Исследуйте, как объединить качества ${planet1} и ${planet2}: ведите дневник наблюдений.`);
            base.push('Фокус на интеграции — маленькие испытания, где вы сознательно проявляете обе стороны.');
        } else if(name === 'Оппозиция'){
            base.push(`Ищите баланс между ${planet1} и ${planet2}: практика «и/и», а не «или».`);
            base.push('Разделяйте пространство и время для проявления каждой стороны: распределяйте задачи и роли.');
        } else if(name === 'Квадратура'){
            base.push(`Работайте с напряжением между ${planet1} и ${planet2} через действие: конкретные пробные шаги.`);
            base.push('Сделайте 30-дневный челлендж для постепенной проработки конфликта.');
        } else if(name === 'Тригон' || name === 'Тригон'){
            base.push(`Используйте естественные таланты, которые дают ${planet1} и ${planet2}, усиливайте их через практику.`);
            base.push('Создайте проекты, где сильные стороны работают в связке — коллаборации, портфолио.');
        } else if(name === 'Секстиль'){
            base.push(`Ищите возможности и приглашения для развития связи между ${planet1} и ${planet2}.`);
            base.push('Будьте открыты к новым знакомствам и обучению — это активирует аспект.');
        } else {
            base.push('Наблюдайте проявления и делайте малые целенаправленные действия для интеграции.');
        }
        return base;
    }

    // Helpers to build HTML blocks
    function wrapCard(title, contentHtml, options){
        const color = (options && options.color) ? options.color : 'var(--accent)';
        return `\n<div class="result-card">\n  <h3 style="color:${color};">${title}</h3>\n  <div>${contentHtml}</div>\n</div>\n`;
    }

    function buildKeyIndicators(chartData){
        const asc = chartData.ascendantSign !== undefined ? (window.ZODIAC_RU ? ZODIAC_RU[chartData.ascendantSign] : 'Asc') : '-';
        const sun = chartData.planets && chartData.planets.sun ? `${ZODIAC_RU[chartData.planets.sun.sign]} ${chartData.planets.sun.degree.toFixed(1)}°` : '-';
        const moon = chartData.planets && chartData.planets.moon ? `${ZODIAC_RU[chartData.planets.moon.sign]} ${chartData.planets.moon.degree.toFixed(1)}°` : '-';
        const mc = chartData.mcSign !== undefined ? (window.ZODIAC_RU ? ZODIAC_RU[chartData.mcSign] : 'MC') : '-';

        const html = `
            <div style="display:flex;gap:12px;flex-wrap:wrap;">
                <div style="flex:1;min-width:180px;padding:12px;background:rgba(255,255,255,0.9);border-radius:10px;border-left:4px solid var(--accent);">
                    <div style="font-weight:700;color:var(--accent);">Асцендент</div>
                    <div style="margin-top:6px">${asc}</div>
                </div>
                <div style="flex:1;min-width:180px;padding:12px;background:rgba(255,255,255,0.9);border-radius:10px;border-left:4px solid var(--accent);">
                    <div style="font-weight:700;color:var(--accent);">Солнце</div>
                    <div style="margin-top:6px">${sun}</div>
                </div>
                <div style="flex:1;min-width:180px;padding:12px;background:rgba(255,255,255,0.9);border-radius:10px;border-left:4px solid var(--accent);">
                    <div style="font-weight:700;color:var(--accent);">Луна</div>
                    <div style="margin-top:6px">${moon}</div>
                </div>
                <div style="flex:1;min-width:180px;padding:12px;background:rgba(255,255,255,0.9);border-radius:10px;border-left:4px solid var(--accent);">
                    <div style="font-weight:700;color:var(--accent);">МС (Средний градус)</div>
                    <div style="margin-top:6px">${mc}</div>
                </div>
            </div>
        `;
        return wrapCard('🔎 Основные показатели', html, {color:'var(--accent-warm)'});
    }

    function buildPlanetsInSigns(chartData, gender){
        if(!chartData.planets) return '';
        let html = '';
        Object.entries(chartData.planets).forEach(([name, data]) => {
            const sign = window.ZODIAC_RU ? ZODIAC_RU[data.sign] : data.sign;
            const interp = (window.getPlanetInSignInterpretation) ? getPlanetInSignInterpretation(name, data.sign, gender) : '';
            const suggestions = getWorkSuggestionsForPlanet(name, data.sign, data.house);
            html += `
                <div style="margin-bottom:12px;padding:12px;border-radius:8px;background:rgba(248,249,250,0.6);">
                    <div style="font-weight:600;color:var(--accent);">${(window.PLANETS_RU && PLANETS_RU[name]) ? PLANETS_RU[name] : name} в ${sign} — ${data.degree.toFixed(1)}°</div>
                    <div style="margin-top:8px;color:var(--text);">${interp}</div>
                    <ul style="margin-top:8px;color:var(--text-muted);">
                        ${suggestions.map(s=>`<li>${s}</li>`).join('')}
                    </ul>
                </div>
            `;
        });
        return wrapCard('🌍 Планеты в знаках', html);
    }

    function buildPlanetsInHouses(chartData, gender){
        if(!chartData.planets) return '';
        let html = '';
        Object.entries(chartData.planets).forEach(([name, data]) =>{
            const interp = (window.getPlanetInHouseInterpretation) ? getPlanetInHouseInterpretation(name, data.house, gender) : '';
            const suggestions = getWorkSuggestionsForPlanet(name, data.sign, data.house);
            html += `
                <div style="margin-bottom:12px;padding:12px;border-radius:8px;background:rgba(255,255,255,0.9);">
                    <div style="font-weight:600;color:var(--accent);">${(window.PLANETS_RU && PLANETS_RU[name]) ? PLANETS_RU[name] : name} в ${data.house}-м доме</div>
                    <div style="margin-top:8px;color:var(--text);">${interp}</div>
                    <div style="margin-top:8px;color:var(--text-muted);">${suggestions.length? '<strong>Практики:</strong> ' + suggestions.join(' · ') : ''}</div>
                </div>
            `;
        });
        return wrapCard('🏠 Планеты в домах', html, {color:'var(--accent)'});
    }

    function buildAspectsList(chartData, gender){
        if(!chartData.aspects || !Array.isArray(chartData.aspects)) return '';
        // Order by importance: Соединение, Оппозиция, Квадратура, Тригон, Секстиль
        const order = { 'Соединение':0, 'Оппозиция':1, 'Квадратура':2, 'Тригон':3, 'Секстиль':4 };
        const sorted = chartData.aspects.slice().sort((a,b)=>{
            const oa = order[a.name]!==undefined?order[a.name]:9;
            const ob = order[b.name]!==undefined?order[b.name]:9;
            return oa - ob || Math.abs(b.orb || 0) - Math.abs(a.orb || 0);
        });

        let html = '';
        sorted.forEach(aspect =>{
            const interp = (window.getAspectInterpretation) ? getAspectInterpretation(aspect, gender) : '';
            const suggestions = getWorkSuggestionsForAspect(aspect);
            const p1 = (window.PLANETS_RU && PLANETS_RU[aspect.planet1]) ? PLANETS_RU[aspect.planet1] : aspect.planet1;
            const p2 = (window.PLANETS_RU && PLANETS_RU[aspect.planet2]) ? PLANETS_RU[aspect.planet2] : aspect.planet2;
            html += `
                <div style="margin-bottom:12px;padding:12px;border-radius:8px;background:rgba(250,250,250,0.7);border-left:4px solid rgba(138,123,168,0.1);">
                    <div style="font-weight:700;color:var(--accent);">${p1} — ${p2} (${aspect.name}${aspect.orb?`, орб ${aspect.orb.toFixed(1)}°`:''})</div>
                    <div style="margin-top:8px;color:var(--text);">${interp}</div>
                    <div style="margin-top:8px;color:var(--text-muted);"><strong>Практика:</strong>
                        <ul>${suggestions.map(s=>`<li>${s}</li>`).join('')}</ul>
                    </div>
                </div>
            `;
        });
        return wrapCard('✨ Основные аспекты и рекомендации', html, {color:'var(--accent-warm)'});
    }

    function buildLifeStages(chartData, gender, userName){
        const childhood = (window.getChildhoodInterpretation) ? getChildhoodInterpretation(chartData, gender, userName) : '';
        const youth = (window.getYouthInterpretation) ? getYouthInterpretation(chartData, gender, userName) : '';
        const current = (window.getCurrentTimeInterpretation) ? getCurrentTimeInterpretation(chartData, gender, userName) : '';
        const html = `
            <div style="margin-bottom:12px;">${childhood}</div>
            <div style="margin-bottom:12px;">${youth}</div>
            <div style="margin-bottom:12px;">${current}</div>
        `;
        return wrapCard('📅 Жизненные этапы', html, {color:'var(--accent)'});
    }

    // Main enhanced renderer
    function enhancedDisplayResults(chartData){
        try{
            const userName = chartData.input?.name || 'Вы';
            const gender = chartData.input?.gender || 'unknown';

            let out = '';
            out += `\n<div style="margin-bottom:16px;padding:16px;background:linear-gradient(90deg, rgba(184,169,212,0.12), rgba(255,197,217,0.06));border-radius:12px;">\n  <div style="font-size:1.15em;font-weight:700;color:var(--accent-warm);">${userName}, ваш краткий психологический профиль</div>\n  <div style="margin-top:8px;color:var(--text);">За 10–20 секунд вы увидите ключевые черты: как вы проявляетесь, что вас мотивирует и где находится ваш ресурс. Формулировки — ясные и практичные, без эзотерики.</div>\n</div>\n`;

            // Key indicators
            out += buildKeyIndicators(chartData);

            // Planets in signs
            out += buildPlanetsInSigns(chartData, gender);

            // Planets in houses
            out += buildPlanetsInHouses(chartData, gender);

            // Aspects + suggestions
            out += buildAspectsList(chartData, gender);

            // Life stages
            out += buildLifeStages(chartData, gender, userName);

            // Practical final block: top 3 recommendations (derived simply)
            const topSuggestions = [];
            // collect from Sun/Moon/Asc/Major aspects
            if(chartData.planets && chartData.planets.sun) topSuggestions.push(...getWorkSuggestionsForPlanet('sun', chartData.planets.sun.sign, chartData.planets.sun.house));
            if(chartData.planets && chartData.planets.moon) topSuggestions.push(...getWorkSuggestionsForPlanet('moon', chartData.planets.moon.sign, chartData.planets.moon.house));
            if(chartData.aspects && chartData.aspects.length) topSuggestions.push(...getWorkSuggestionsForAspect(chartData.aspects[0]));

            const finalHtml = `\n<div class="result-card" style="border-left:4px solid var(--success);">\n  <h3 style="color:var(--success);">🛠 Практические шаги</h3>\n  <ol>\n    ${topSuggestions.slice(0,5).map(s=>`<li style="margin-bottom:8px;color:var(--text);">${s}</li>`).join('')}\n  </ol>\n  <div style="color:var(--text-muted);font-size:0.95em;margin-top:8px;">Рекомендуется выбирать 1–2 практики на месяц и отслеживать изменения.</div>\n</div>\n`;

            out += finalHtml;

            // Inject into page
            const resultsSection = safeGet('resultsSection');
            if(resultsSection){
                resultsSection.innerHTML = out;
                resultsSection.style.display = 'grid';
            }

            // Re-populate smaller blocks the original app expects
            const interpretationEl = safeGet('interpretation');
            if(interpretationEl){
                interpretationEl.innerHTML = `<div style="color:var(--text);line-height:1.6;">${userName}, ниже развернутое содержание вашей карты и практические рекомендации.</div>`;
            }

            const planetsInSignsEl = safeGet('planetsInSigns');
            if(planetsInSignsEl){ planetsInSignsEl.innerHTML = ''; }
            const planetsInHousesEl = safeGet('planetsInHouses');
            if(planetsInHousesEl){ planetsInHousesEl.innerHTML = ''; }
            const aspectsListEl = safeGet('aspectsList');
            if(aspectsListEl){ aspectsListEl.innerHTML = ''; }

            // Ensure ascendant value updated if available
            if(chartData.ascendantSign !== undefined && safeGet('ascendentValue')){
                safeGet('ascendentValue').textContent = `${(window.ZODIAC_RU?ZODIAC_RU[chartData.ascendantSign]:'-')} ${(chartData.ascendant%30)?.toFixed?chartData.ascendant%30.toFixed(1):''}°`;
            }

            console.info('enhancedDisplayResults: rendered enhanced output');
        }catch(e){
            console.error('enhancedDisplayResults error', e);
        }
    }

    onReady(function(){
        // Expose helpers globally for debugging/consumption by existing code
        window.getWorkSuggestionsForPlanet = getWorkSuggestionsForPlanet;
        window.getWorkSuggestionsForAspect = getWorkSuggestionsForAspect;
        // Override displayResults
        window.displayResults = enhancedDisplayResults;
        console.info('natal_interpretations.js loaded: displayResults overridden');
    });
})();
