import sys,re
f=sys.argv[1]; h=open(f).read()
def rep(a,b):
    global h
    assert h.count(a)==1,(h.count(a),a[:90]); h=h.replace(a,b)

# ---- SKY: sunrise palette, uWater
rep("uniform vec3 uSun;uniform float uMode;uniform float uTime;\n","uniform vec3 uSun;uniform float uMode;uniform float uTime;uniform float uWater;\n")
rep("vec3 skyBase(vec3 d){return mix(skyDay(d),skyNight(d),uMode);}`;",
"""vec3 skyRise(vec3 d){float y=max(d.y,0.);float s=max(dot(d,uSun),0.);float fa=max(dot(normalize(d.xz+1e-5),normalize(uSun.xz+1e-5)),0.);
 vec3 zen=vec3(0.09,0.18,0.46);vec3 mid=mix(vec3(0.36,0.32,0.55),vec3(0.92,0.50,0.42),pow(fa,2.));
 vec3 hor=mix(vec3(0.66,0.52,0.62),vec3(1.30,0.74,0.36),pow(fa,3.));
 vec3 c=mix(hor,mid,smoothstep(0.,0.13,y));c=mix(c,zen,smoothstep(0.09,0.7,y));
 return c+vec3(1.2,0.66,0.28)*pow(s,10.)*0.7+vec3(1.,0.75,0.45)*pow(s,3.)*0.18*exp(-y*4.);}
vec3 skyBase(vec3 d){return mix(mix(skyDay(d),skyNight(d),uMode),skyRise(d),uWater);}`;""")
rep("float f=1.-exp(-length(v)*mix(0.0028,0.011,uMode));","float f=1.-exp(-length(v)*mix(mix(0.0028,0.011,uMode),0.0045,uWater));")
rep("vec3 sunC=vec3(1.,0.95,0.84)*28.;","vec3 sunC=mix(vec3(1.,0.95,0.84)*28.,vec3(1.,0.72,0.42)*24.,uWater);")
rep("c+=mix(vec3(1.,0.85,0.6)*(exp(-ang*18.)*0.9+exp(-ang*70.)*1.6),","c+=mix(mix(vec3(1.,0.85,0.6),vec3(1.,0.6,0.3),uWater)*(exp(-ang*18.)*0.9+exp(-ang*70.)*1.6),")
rep("c=mix(c,mix(cd,cn,uMode),cov*mix(1.,0.75,uMode));",
    "vec3 cw=mix(vec3(0.42,0.34,0.52),vec3(1.45,1.02,0.78),lit);c=mix(c,mix(mix(cd,cn,uMode),cw,uWater),cov*mix(1.,0.75,uMode));")
rep("c+=vec3(0.85,0.88,1.)*st*1.2*uMode*(1.-cov);}","c+=vec3(0.85,0.88,1.)*st*1.2*uMode*(1.-uWater)*(1.-cov);}")
rep("if(uPanoOn>0.5){vec4 pm=panoW(uCam,d);","if(uPanoOn>0.5&&uWater<0.5){vec4 pm=panoW(uCam,d);")

# ---- ocean program
ocean=r''' ocean:prog(`layout(location=0) in vec2 aP;uniform mat4 uVP;uniform float uTime;out vec3 vW;
  void main(){vec2 p=aP;float y=0.2+0.06*sin(dot(p,vec2(0.21,0.13))+uTime*0.9)+0.045*sin(dot(p,vec2(-0.17,0.29))+uTime*1.1)+0.025*sin(dot(p,vec2(0.41,-0.33))+uTime*1.6);
   vW=vec3(p.x,y,p.y);gl_Position=uVP*vec4(vW,1.);}`,
  `in vec3 vW;out vec4 o;uniform vec3 uPtr;uniform float uGlow;${NOISE}${SKY}${LIGHT}
  vec2 wg(vec2 p,float t){vec2 g=vec2(0.);for(int i=0;i<11;i++){float fi=float(i);float a=fi*2.399+0.4;vec2 dr=vec2(cos(a),sin(a));
    float k=0.32*pow(1.36,fi);float A=0.085/pow(1.5,fi);float ph=dot(dr,p)*k+t*sqrt(9.8*k)+fi*1.7;g+=dr*k*A*cos(ph);}return g;}
  bool hitE(vec3 ro,vec3 rd,vec3 c,vec3 r){vec3 oc=(ro-c)/r,dd=rd/r;float a=dot(dd,dd),b=dot(oc,dd),cc=dot(oc,oc)-1.;float q=b*b-a*cc;return q>0.&&(-b-sqrt(q))>0.;}
  void main(){float dist=length(vW-uCam);vec2 g=wg(vW.xz,uTime);
   vec2 tp=vW.xz-uPtr.xy;float r=length(tp);if(r>0.01)g+=tp/r*cos(r*6.5-uTime*4.5)*0.22*uPtr.z*exp(-r*0.55);
   g*=1./(1.+dist*0.035);vec3 n=normalize(vec3(-g.x,1.,-g.y));vec3 v=normalize(uCam-vW);
   vec3 rr=reflect(-v,n);rr.y=abs(rr.y)+0.002;rr=normalize(rr);
   float fr=0.02+0.98*pow(1.-max(dot(n,v),0.),5.);vec3 refl=skyBase(rr);
   refl+=uSunCol*pow(max(dot(rr,uSun),0.),mix(1400.,160.,smoothstep(6.,70.,dist)))*mix(7.,3.,smoothstep(6.,70.,dist));
   float sc=0.;if(hitE(vW,rr,vec3(-0.18,0.4,-0.27),vec3(2.45,1.9,1.95)))sc=1.;else if(hitE(vW,rr,vec3(0.1,2.6,0.),vec3(0.95,0.55,0.95)))sc=1.;else if(hitE(vW,rr,vec3(0.17,3.75,0.22),vec3(0.8,0.82,0.86)))sc=1.;
   refl=mix(refl,vec3(1.,0.97,0.92)*2.4*uGlow,sc*0.8);
   vec3 deep=vec3(0.006,0.05,0.085);vec3 sss=vec3(0.02,0.16,0.18)*(uSunCol*0.18+uSky*0.6)*clamp(0.4+(vW.y-0.2)*5.,0.,1.);
   vec3 c=mix(deep*(uSky+0.25)+sss+bodyLight(vW)*vec3(0.06,0.14,0.15),refl,fr);
   float e=length((vW.xz-uBodyC)/uBodyR);float fm=(1.-smoothstep(0.95,1.4,e))*smoothstep(0.38,0.72,noise(vW.xz*3.2+uTime*0.5)+0.25*(1.-e));
   c=mix(c,(uSky*0.8+uSunCol*0.35)*0.9,clamp(fm,0.,1.)*0.7);
   o=vec4(fogit(c,vW),1.);}`),
'''
i=h.index(' fig:prog('); h=h[:i]+ocean+h[i:]

# ---- particles: colour/shape per mode
rep("ff:prog(`layout(location=0) in vec4 aP;uniform mat4 uVP;uniform mat4 uV;uniform float uTime;uniform float uH;uniform float uVis;out float vB;",
    "ff:prog(`layout(location=0) in vec4 aP;uniform mat4 uVP;uniform mat4 uV;uniform float uTime;uniform float uH;uniform float uVis;uniform float uFFS;out float vB;")
rep("gl_PointSize=clamp(uH*0.05*","gl_PointSize=clamp(uFFS*uH*0.05*")
rep("`in float vB;out vec4 o;void main(){vec2 q=gl_PointCoord-0.5;float r=length(q)*2.;\n   float a=(exp(-r*r*20.)+exp(-r*r*4.)*0.22)*(1.-smoothstep(0.8,1.,r));o=vec4(vec3(0.6,1.,0.3)*a*vB*6.,1.);}`",
    "`in float vB;out vec4 o;uniform vec3 uFFC;uniform float uFFK;void main(){vec2 q=gl_PointCoord-0.5;float r=length(q)*2.;\n   float a=(exp(-r*r*20.*uFFK)+exp(-r*r*4.)*0.22/uFFK)*(1.-smoothstep(0.8,1.,r));o=vec4(uFFC*a*vB*6.,1.);}`")

# ---- uniforms
rep("u.uBake&&gl.uniform1f(u.uBake,S.bake?1:0);}","u.uBake&&gl.uniform1f(u.uBake,S.bake?1:0);u.uWater&&gl.uniform1f(u.uWater,S.water||0);}")
rep("const LS={VP,eye,t,SUN,SC,SK,md,BL:BL*glow,swarm};","const LS={VP,eye,t,SUN,SC,SK,md,BL:BL*glow,swarm,water:wat};")

# ---- constants
rep("const SUN_D=nrm(rotY([0.75,0.62,0.35],TURN)), DUSK_D=nrm([0.12,0.11,-0.99]);",
    "const SUN_D=nrm(rotY([0.75,0.62,0.35],TURN)), DUSK_D=nrm([0.12,0.11,-0.99]);\n// sunrise over the ocean: low sun ahead-right of the start view, so the glitter path runs toward the camera\nconst RISE_D=(()=>{const th=0.63+TURN,fw=[-Math.sin(th),0,-Math.cos(th)],sd=[Math.cos(th),0,-Math.sin(th)];return nrm([fw[0]*0.92+sd[0]*0.36,0.075,fw[2]*0.92+sd[2]*0.36]);})();\nconst RISE={sun:[2.3,1.45,0.8],sky:[0.30,0.28,0.40],bodyL:1.3,exp:0.95};")

# ---- frame: mode blending incl. water
rep("mode+=((night?1:0)-mode)*(1-Math.exp(-dt*(reduce?6:1.8)));const md=mode*mode*(3-2*mode);\n  const SUN=nrm(mix(SUN_D,MOON_D,md)),SC=mix(DAY.sun,NIGHT.sun,md),SK=mix(DAY.sky,NIGHT.sky,md);\n  const BL=DAY.bodyL+(NIGHT.bodyL-DAY.bodyL)*md,EXPO=DAY.exp+(NIGHT.exp-DAY.exp)*md;",
"""if(trans.ph==='out'){trans.v-=dt/0.5;if(trans.v<=0){trans.v=0;wat=water?1:0;trans.ph='in';if(wat)mode=0;}}else if(trans.ph==='in'){trans.v+=dt/0.8;if(trans.v>=1){trans.v=1;trans.ph=null;}}
  mode+=((night&&!wat?1:0)-mode)*(1-Math.exp(-dt*(reduce?6:1.8)));const md=mode*mode*(3-2*mode);
  let SUN=nrm(mix(SUN_D,MOON_D,md)),SC=mix(DAY.sun,NIGHT.sun,md),SK=mix(DAY.sky,NIGHT.sky,md);
  let BL=DAY.bodyL+(NIGHT.bodyL-DAY.bodyL)*md,EXPO=DAY.exp+(NIGHT.exp-DAY.exp)*md;
  if(wat){SUN=RISE_D;SC=RISE.sun;SK=RISE.sky;BL=RISE.bodyL;EXPO=RISE.exp;}""")
rep("gl.uniform3fv(P.sky.u.uCel,CEL);","gl.uniform3fv(P.sky.u.uCel,wat?RISE_D:CEL);")
rep("gl.useProgram(P.ground.p);common(P.ground.u);","if(!wat){gl.useProgram(P.ground.p);common(P.ground.u);")
rep("gl.useProgram(P.fig.p);common(P.fig.u);",
    "}else{gl.useProgram(P.ocean.p);common(P.ocean.u);gl.uniform3f(P.ocean.u.uPtr,ptrW[0],ptrW[2],ptrA);gl.uniform1f(P.ocean.u.uGlow,glow);gl.bindVertexArray(gVAO);gl.drawElements(gl.TRIANGLES,gi.length,gl.UNSIGNED_INT,0);}\n  gl.useProgram(P.fig.p);common(P.fig.u);")
rep("gl.useProgram(P.grass.p);common(P.grass.u);","if(!wat){gl.useProgram(P.grass.p);common(P.grass.u);")
rep("  if(flyScale>0.01){gl.enable(gl.BLEND);","  }\n  if(flyScale>0.01&&!wat){gl.enable(gl.BLEND);")
rep("if(md>0.01){gl.depthMask(false);gl.enable(gl.BLEND);gl.blendFunc(gl.ONE,gl.ONE);\n    gl.useProgram(P.ff.p);common(P.ff.u);gl.uniformMatrix4fv(P.ff.u.uV,false,V);gl.uniform1f(P.ff.u.uH,H);gl.uniform1f(P.ff.u.uVis,md);",
    "if(md>0.01||wat){gl.depthMask(false);gl.enable(gl.BLEND);gl.blendFunc(gl.ONE,gl.ONE);\n    gl.useProgram(P.ff.p);common(P.ff.u);gl.uniformMatrix4fv(P.ff.u.uV,false,V);gl.uniform1f(P.ff.u.uH,H);gl.uniform1f(P.ff.u.uVis,wat?0.85:md);\n    if(wat){gl.uniform3f(P.ff.u.uFFC,1.0,0.86,0.72);gl.uniform1f(P.ff.u.uFFS,0.55);gl.uniform1f(P.ff.u.uFFK,2.2);}else{gl.uniform3f(P.ff.u.uFFC,0.6,1.,0.3);gl.uniform1f(P.ff.u.uFFS,1.);gl.uniform1f(P.ff.u.uFFK,1.);}")
rep("const fade=Math.min(1,(now-t0)/1600);","const fade=Math.min(1,(now-t0)/1600)*(0.08+0.92*trans.v*trans.v*(3-2*trans.v));")

# ---- UI / state
rep("""<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg></button>""",
"""<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg></button>
      <button id="mWater" aria-pressed="false" aria-label="Ocean" title="Ocean"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M2.5 9.5c1.6-1.6 3.2-1.6 4.8 0s3.2 1.6 4.8 0 3.2-1.6 4.8 0 3.2 1.6 4.6 0"/><path d="M2.5 14.5c1.6-1.6 3.2-1.6 4.8 0s3.2 1.6 4.8 0 3.2-1.6 4.8 0 3.2 1.6 4.6 0"/></svg></button>""")
rep("let night=/night/.test(location.hash)||(!/day/.test(location.hash)&&(hr<6||hr>=19)),mode=night?1:0;",
    "let night=/night/.test(location.hash)||(!/day|ocean/.test(location.hash)&&(hr<6||hr>=19)),mode=night?1:0;\nlet water=/ocean/.test(location.hash),wat=water?1:0;const trans={v:1,ph:null};if(water)mode=0;")
rep("const bDay=document.getElementById('mDay'),bNight=document.getElementById('mNight'),hint=document.getElementById('hint');",
    "const bDay=document.getElementById('mDay'),bNight=document.getElementById('mNight'),bWater=document.getElementById('mWater'),hint=document.getElementById('hint');")
i=h.index("function setMode(n){"); j=h.index("cv.addEventListener('pointermove'")
h=h[:i]+"""function setMode(m){const w=m==='ocean';if(m==='night')night=true;if(m==='day')night=false;
  if(w!==water){water=w;trans.ph='out';}
  bDay.setAttribute('aria-pressed',m==='day');bNight.setAttribute('aria-pressed',m==='night');bWater.setAttribute('aria-pressed',w);
  document.body.classList.toggle('night',m==='night');document.body.classList.toggle('ocean',w);
  hint.textContent=w?'(Move) (Drag) — ripples and droplets follow you':m==='night'?'(Move) (Drag) — the fireflies follow you':'(Move) (Drag) — the dragonflies follow you';}
setMode(water?'ocean':night?'night':'day');bDay.onclick=()=>setMode('day');bNight.onclick=()=>setMode('night');bWater.onclick=()=>setMode('ocean');
"""+h[j:]
rep('aria-label="Light or dark"','aria-label="Scene mode"')
open(f,'w').write(h)
open('/tmp/v2.js','w').write(re.findall(r'<script>(.*?)</script>',h,re.S)[0]); print('ok')
