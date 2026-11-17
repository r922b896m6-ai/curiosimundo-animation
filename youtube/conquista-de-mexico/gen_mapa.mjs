import fs from 'fs';
import * as topojson from 'topojson-client';
import * as d3 from 'd3-geo';
const topo = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
const feats = topojson.feature(topo, topo.objects.countries).features;
const byName = n => feats.filter(f => f.properties.name === n);
const G = { 'MÉXICO': ['Mexico'], 'CENTROAMÉRICA': ['Guatemala', 'Belize', 'Honduras', 'El Salvador', 'Nicaragua'], CUBA: ['Cuba'], OTROS: ['United States of America', 'Bahamas', 'Jamaica', 'Haiti', 'Cayman Is.'] };
const p = d3.geoMercator(); p.fitExtent([[40, 40], [1880, 1040]], { type: 'Feature', geometry: { type: 'MultiPoint', coordinates: [[-101, 15.5], [-78, 15.5], [-101, 24.2], [-78, 24.2]] } });
const path = d3.geoPath(p), out = { groups: {}, cities: {}, lines: {} };
for (const [g, names] of Object.entries(G)) out.groups[g] = names.flatMap(byName).map(f => path(f)).filter(Boolean).join(' ');
const lake = [[-99.17, 19.6], [-99.05, 19.67], [-98.95, 19.61], [-98.92, 19.48], [-98.98, 19.38], [-99.05, 19.29], [-99.12, 19.26], [-99.19, 19.33], [-99.17, 19.46]];
out.groups.LAGO = 'M' + lake.map(c => p(c).map(v => v.toFixed(1)).join(' ')).join(' L') + 'Z';
const C = { Cuba: [-79.5, 21.8], Cozumel: [-86.95, 20.45], Centla: [-92.6, 18.45], Veracruz: [-96.25, 19.3], Cempoala: [-96.4, 19.45], Tlaxcala: [-98.24, 19.31], Cholula: [-98.3, 19.06],
  'Paso de Cortés': [-98.66, 19.1], Popocatépetl: [-98.62, 19.02], Iztaccíhuatl: [-98.64, 19.18], Tenochtitlan: [-99.13, 19.43], Texcoco: [-98.88, 19.51], Tlacopan: [-99.19, 19.47], Otumba: [-98.75, 19.7],
  Iztapalapa: [-99.06, 19.36], Tlatelolco: [-99.135, 19.455], Chapultepec: [-99.19, 19.42], Tepeyac: [-99.12, 19.49], Nojpetén: [-89.88, 16.93], Tabasco: [-92.9, 18.0] };
for (const [k, v] of Object.entries(C)) out.cities[k] = p(v).map(x => Math.round(x * 10) / 10);
const L = { mar: [[-84.95, 21.87], [-86.95, 20.5], [-87.5, 21.5], [-90.4, 21.3], [-90.6, 19.8], [-92.6, 18.45], [-94.5, 18.6], [-96.15, 19.25]],
  tierra: [[-96.25, 19.3], [-96.4, 19.45], [-97.0, 19.6], [-97.7, 19.45], [-98.24, 19.31], [-98.3, 19.06], [-98.66, 19.1], [-98.95, 19.28], [-99.06, 19.36], [-99.13, 19.43]],
  noche: [[-99.13, 19.43], [-99.19, 19.47], [-99.21, 19.6], [-99.05, 19.76], [-98.75, 19.7], [-98.5, 19.55], [-98.24, 19.31]],
  narvaez: [[-82.5, 21.9], [-88, 22.6], [-93.5, 21.2], [-96.2, 19.4]], acempoala: [[-99.13, 19.43], [-98.95, 19.28], [-98.3, 19.06], [-97.7, 19.45], [-97.0, 19.6], [-96.4, 19.45]],
  cTacuba: [[-99.13, 19.43], [-99.19, 19.47]], cIztapalapa: [[-99.13, 19.43], [-99.06, 19.36]], cTepeyac: [[-99.13, 19.43], [-99.12, 19.49]], agua: [[-99.19, 19.42], [-99.13, 19.43]],
  regreso: [[-98.24, 19.31], [-98.6, 19.45], [-98.88, 19.51]] };
for (const [k, pts] of Object.entries(L)) out.lines[k] = 'M' + pts.map(q => p(q).map(x => x.toFixed(1)).join(' ')).join(' L');
fs.writeFileSync(process.argv[2] + '/mexico1519.json', JSON.stringify(out));
console.log(out.cities.Tenochtitlan, out.cities.Veracruz, out.cities.Cuba, out.cities.Centla);
