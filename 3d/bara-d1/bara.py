import numpy as np, struct, math, sys
from skimage import measure
H=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
# ---- parametri (mm): BARA, difuzor | Puck | difuzor ----
W,D,HT=170.0,70.0,64.0; WALL=2.4; FRONT=3.6; BODY_D=D-WALL
XP=85.0; XL,XR=25.0,145.0; ZC=32.0
DIV=[47.4,122.6]                      # axele peretilor despartitori (grosime 2.4)
PUCK_R=22.9; LIP_R=19.5; TUBE_R=26.0; TUBE_L=26.5
SP_R=20.25; OPEN_R=17.5; SP_FL=2.5; GRILLE=1.6; RS=GRILLE+SP_FL; RE=RS+2.5   # difuzor Ø40 x 20, flansa ~2.5 (de verificat)
f32=np.float32
def hyp(a,b): return np.sqrt(a*a+b*b)
def rbox(x,y,z,lo,hi,r=0.0):
    c=[(lo[i]+hi[i])/2 for i in range(3)]; h=[(hi[i]-lo[i])/2-r for i in range(3)]
    qx=np.abs(x-c[0])-h[0]; qy=np.abs(y-c[1])-h[1]; qz=np.abs(z-c[2])-h[2]
    out=np.sqrt(np.maximum(qx,0)**2+np.maximum(qy,0)**2+np.maximum(qz,0)**2)
    return out+np.minimum(np.maximum(np.maximum(qx,qy),qz),0)-r
def cylY(x,y,z,cx,cz,r,y0,y1): return np.maximum(hyp(x-cx,z-cz)-r,np.maximum(y0-y,y-y1))
def cylZ(x,y,z,cx,cy,r,z0,z1): return np.maximum(hyp(x-cx,y-cy)-r,np.maximum(z0-z,z-z1))
def cylX(x,y,z,cy,cz,r,x0,x1): return np.maximum(hyp(y-cy,z-cz)-r,np.maximum(x0-x,x-x1))
def rect_xz(x,z,cx,cz,hx,hz,r):
    qx=np.abs(x-cx)-(hx-r); qz=np.abs(z-cz)-(hz-r)
    return np.sqrt(np.maximum(qx,0)**2+np.maximum(qz,0)**2)+np.minimum(np.maximum(qx,qz),0)-r
def seg_xz(x,z,a,b,r):
    ax,az=a;bx,bz=b;dx,dz=bx-ax,bz-az;L=dx*dx+dz*dz
    t=np.clip(((x-ax)*dx+(z-az)*dz)/L,0,1)
    return hyp(x-(ax+t*dx),z-(az+t*dz))-r
def U(*a):
    r=a[0]
    for b in a[1:]: r=np.minimum(r,b)
    return r
def S(a,b): return np.maximum(a,-b)
def LUGS(cx): return [(cx,ZC+24.5),(cx,ZC-24.5)]
POSTS=[(7.0,7.0),(W-7.0,7.0),(7.0,HT-7.0),(W-7.0,HT-7.0)]+[(d,7.0) for d in DIV]+[(d,HT-7.0) for d in DIV]
CH=4.0
def OUT(x,y,z):
    d2=rect_xz(x,z,W/2,HT/2,W/2,HT/2,9)
    A=np.maximum(np.maximum(d2,d2-y+CH),-y)
    return np.maximum(A,rbox(x,y,z,(0,-400,0),(W,D,HT),5))
def body(x,y,z):
    outer=np.maximum(OUT(x,y,z),y-BODY_D)
    cav=rbox(x,y,z,(WALL,FRONT,WALL),(W-WALL,200,HT-WALL),6.6)
    s=S(outer,cav)
    add=[cylY(x,y,z,XP,ZC,TUBE_R,0,TUBE_L)]
    for d in DIV: add.append(rbox(x,y,z,(d-1.2,FRONT-.5,WALL-.5),(d+1.2,BODY_D,HT-WALL+.5)))
    for cx in (XL,XR): add.append(np.maximum(cylY(x,y,z,cx,ZC,29,FRONT-.5,RE),outer+1.0))
    for px,pz in POSTS: add.append(cylY(x,y,z,px,pz,4.5,FRONT-.5,BODY_D))
    add.append(rbox(x,y,z,(50,29,WALL-.5),(121,58,5.4)))                       # pad placi
    add.append(rbox(x,y,z,(XP-7.3,34.7,HT-WALL-8.0),(XP+7.3,49.3,HT-WALL+.5)))  # cos microfon
    s=np.maximum(U(s,*add),outer)
    cut=[cylY(x,y,z,XP,ZC,PUCK_R,1.2,TUBE_L+1),
         cylY(x,y,z,XP,ZC,LIP_R,-1,1.3),
         rbox(x,y,z,(XP-19.5,3.5,ZC-TUBE_R-1),(XP+19.5,15.5,ZC-10)),            # fereastra USB-C + butoane
         cylZ(x,y,z,XP,42,0.8,HT-WALL-1,HT+1),                                  # gaura microfon
         rbox(x,y,z,(XP-6.7,35.3,HT-WALL-6.0),(XP+6.7,48.7,HT-WALL-1.2)),
         rbox(x,y,z,(62-9.2,31,4.2),(62+9.2,54.9,6)),                           # locas ESP
         rbox(x,y,z,(88-8.95,33,4.2),(88+8.95,52.4,6)),                         # locas MAX stanga
         rbox(x,y,z,(110-8.95,33,4.2),(110+8.95,52.4,6))]                       # locas MAX dreapta
    for d in DIV: cut.append(cylX(x,y,z,40,20,2.5,d-3,d+3))                      # trecere fire difuzor
    for cx in (XL,XR):
        cut.append(cylY(x,y,z,cx,ZC,OPEN_R,-1,GRILLE+.2))                       # deschidere libera (fara grila)
        cut.append(cylY(x,y,z,cx,ZC,SP_R,GRILLE,RE+.1))                         # locas difuzor
        for lx,lz in LUGS(cx):
            cut.append(np.maximum(seg_xz(x,z,(cx,ZC),(lx,lz),3.6),np.maximum(RS-y,y-(RE+.1))))
            cut.append(cylY(x,y,z,lx,lz,1.1,GRILLE+.3,RS+.1))
    for px,pz in POSTS: cut.append(cylY(x,y,z,px,pz,1.3,BODY_D-14,BODY_D+1))
    for fx,fy in ((15,15),(W-15,15),(15,BODY_D-15),(W-15,BODY_D-15)): cut.append(cylZ(x,y,z,fx,fy,4.6,-1,1.2))
    return S(s,U(*cut))
def cover(x,y,z):
    plate=np.maximum(OUT(x,y,z),BODY_D-y)
    inner=np.maximum(rect_xz(x,z,W/2,HT/2,W/2-WALL-.25,HT/2-WALL-.25,6.35),np.maximum(BODY_D-3-y,y-BODY_D))
    inner=S(inner,np.maximum(rect_xz(x,z,W/2,HT/2,W/2-WALL-.25-1.6,HT/2-WALL-.25-1.6,4.75),np.maximum(BODY_D-4-y,y-BODY_D-1)))
    s=U(plate,inner)
    for d in DIV: s=U(s,rbox(x,y,z,(d-1.2,BODY_D-3,WALL+.25),(d+1.2,BODY_D+.01,HT-WALL-.25)))   # sigileaza camerele
    for px,pz in POSTS:
        s=S(s,cylY(x,y,z,px,pz,4.9,BODY_D-4,BODY_D+.001))
        s=S(s,cylY(x,y,z,px,pz,1.75,BODY_D-4,D+1))
        s=S(s,cylY(x,y,z,px,pz,3.1,D-1.3,D+1))
    s=S(s,cylY(x,y,z,XP,30.0,6.0,BODY_D-4,D+1))    # mufa DC-022
    return s
def ring(x,y,z):      # inel fixare difuzor, centrat la XL; se printeaza 2 buc
    cx=XL
    r=np.maximum(np.maximum(hyp(x-cx,z-ZC)-20.0,18.0-hyp(x-cx,z-ZC)),np.maximum(RS-y,y-RE))
    parts=[r]
    for lx,lz in LUGS(cx):
        p=np.maximum(seg_xz(x,z,(cx,ZC),(lx,lz),3.4),np.maximum(RS-y,y-RE))
        p=S(p,cylY(x,y,z,lx,lz,1.2,RS-2,RE+1)); parts.append(p)
    return U(*parts)
def mesh(fn,lo,hi,name):
    xs=np.arange(lo[0]-2*H,hi[0]+2*H,H,dtype=f32);ys=np.arange(lo[1]-2*H,hi[1]+2*H,H,dtype=f32);zs=np.arange(lo[2]-2*H,hi[2]+2*H,H,dtype=f32)
    X,Y,Z=np.meshgrid(xs,ys,zs,indexing='ij',sparse=True)
    F=fn(X,Y,Z).astype(f32)
    v,f,_,_=measure.marching_cubes(F,0.0,spacing=(H,H,H))
    e=np.sort(np.concatenate([f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]]),axis=1); _,cnt=np.unique(e,axis=0,return_counts=True); print('  muchii deschise:',int((cnt!=2).sum()))
    v=v+np.array([xs[0],ys[0],zs[0]],dtype=f32)
    tri=v[f]; n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]); l=np.linalg.norm(n,axis=1,keepdims=True); n=n/np.where(l==0,1,l)
    vol=np.sum(np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2])))/6
    with open(name,'wb') as fh:
        fh.write(b'bara D1'.ljust(80,b' '));fh.write(struct.pack('<I',len(f)))
        rec=np.zeros(len(f),dtype=[('n','<f4',3),('v','<f4',(3,3)),('a','<u2')]); rec['n']=n; rec['v']=tri
        fh.write(rec.tobytes())
    print(name,len(f),'tri, volum material %.1f cm3'%(vol/1000), 'bbox',v.min(0).round(1),v.max(0).round(1)); return F,xs,ys,zs
if __name__=='__main__':
    Fb,xs,ys,zs=mesh(body,(0,0,0),(W,BODY_D,HT),'D1_01_corp.stl')
    mesh(cover,(0,BODY_D-4,0),(W,D,HT),'D1_02_capac_spate.stl')
    mesh(ring,(XL-24,RS-2,ZC-34),(XL+24,RE+1,ZC+34),'D1_03_inel_difuzor_x2.stl')
    X,Y,Z=np.meshgrid(xs,ys,zs,indexing='ij',sparse=True)
    m=(Fb>0)&(X>WALL)&(X<DIV[0]-1.2)&(Y>FRONT)&(Y<BODY_D)&(Z>WALL)&(Z<HT-WALL)
    print('camera difuzor liber ~ %.0f cm3 (inainte de difuzor ~ %.0f cm3)'%(m.sum()*H**3/1000, math.pi*20**2*18/1000))
