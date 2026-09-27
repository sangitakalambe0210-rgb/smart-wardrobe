import streamlit as st
import random
st.set_page_config(page_title="Smart Wardrobe AI Pro", page_icon="👗", layout="wide")
st.markdown("""<style>.dress-card{background:white;border-radius:12px;padding:15px;box-shadow:0 4px 12px rgba(0,0,0,0.15);text-align:center;margin-bottom:15px;border:1px solid #eee}.green-box{background:#E8F5E9;border-radius:12px;padding:15px;border-left:5px solid #4CAF50}.pink-box{background:#FCE4EC;border-radius:12px;padding:15px;border-left:5px solid #E91E63}.yellow-box{background:#FFF9C4;border-radius:12px;padding:15px;border-left:5px solid #FFC107}</style>""", unsafe_allow_html=True)
if 'wishlist' not in st.session_state: st.session_state.wishlist=[]
if 'sel_body' not in st.session_state: st.session_state.sel_body="Pear"
if 'sel_skin' not in st.session_state: st.session_state.sel_skin="Wheatish"
if 'sel_under' not in st.session_state: st.session_state.sel_under="Warm"
smart_colors={"Fair":["Pastel Pink","Lavender","Sky Blue","Mint","Beige"],"Wheatish":["Mustard","Olive","Teal","Rust","Wine"],"Dusky":["Royal Blue","Emerald","Wine","Gold","Red"],"Deep":["Cobalt Blue","Ruby Red","Emerald","Black","White"]}

def get_wardrobe():
    base=[{"id":1,"gender":"Female","body":["Hourglass","Rectangle"],"skin":["Fair","Wheatish"],"under":["Cool","Neutral"],"style":"Traditional","type":"Saree - Silk","season":["Festive","Winter","All Season"],"occasion":["Wedding","Festive","Temple"],"name":"Royal Red Silk Saree","color":"Red and Gold","reason":"Perfect drape"},{"id":2,"gender":"Female","body":["Pear","Apple"],"skin":["Wheatish","Dusky"],"under":["Warm","Neutral"],"style":"Traditional","type":"Anarkali Suit","season":["Summer","All Season"],"occasion":["Party","Festive","Temple"],"name":"Mustard Anarkali","color":"Mustard","reason":"Anarkali hides lower body"},{"id":10,"gender":"Male","body":["Trapezoid","Rectangle"],"skin":["Wheatish","Dusky"],"under":["Warm","Neutral"],"style":"Traditional","type":"Kurta Pajama","season":["Festive","Winter"],"occasion":["Wedding","Festive","Temple"],"name":"White Chikankari Kurta","color":"White","reason":"Fitted kurta"}]
    styles_f={"Traditional":["Saree - Silk","Lehenga Choli","Salwar Kameez","Anarkali Suit","Sharara","Palazzo Suit","Kurta Palazzo","Banarasi Saree","Patiala Suit","Long Gown","Phulkari Suit","Chikankari Saree","Ghagra Choli","Chanderi Saree","Kanchipuram Saree","Sambalpuri Suit","Maheshwari Suit","Paithani Saree","Bandhani Saree","Kalamkari Anarkali"],"Indo-Western":["Dhoti plus Crop Top","Palazzo Saree","Kurta with Jeans","Cape Lehenga","Jacket Lehenga","Saree with Belt","Dhoti Pants plus Kurti","Sharara plus Crop Top","Ruffle Saree","Co-ord Set","Kurta with Palazzo","Saree Gown","Dhoti Saree","Peplum with Sharara","Long Jacket with Lehenga","Drape Saree","Fusion Gown","Crop Top with Dhoti Skirt","Kurta Dress with Belt","Co-ord with Cape"],"Western":["Bodycon Dress","A-Line Dress","Maxi Dress","Jumpsuit","Skirt plus Top","Blazer Dress","Shirt Dress","Midi Dress","Off-Shoulder Gown","Denim Dress","Peplum Dress","Culotte Jumpsuit","Slip Dress","Wrap Dress","Pencil Skirt plus Blouse","Playsuit","Tunic Dress","Co-ord Blazer Set","Kimono Dress","Corset Top plus Jeans"]}
    styles_m={"Traditional":["Kurta Pajama","Sherwani","Dhoti Kurta","Pathani Suit","Bandhgala","Kurta plus Nehru Jacket","Lungi plus Shirt","Angarkha","Churidar Kurta","Modi Jacket","Kurta Dhoti","Achkan","Lungi Kurta","Peshawari Suit","Aligarhi Kurta","Mundu plus Shirt","Jodhpuri Bandhgala","Embroidered Kurta","Sadri Jacket","Mysore Peta plus Sherwani"],"Indo-Western":["Nehru Jacket plus Kurta","Kurta plus Jeans","Jodhpuri Suit","Short Kurta plus Trouser","Bandhgala plus Jeans","Kurta plus Waistcoat","Indo-Western Sherwani","Printed Kurta Set","Asymmetric Kurta","Cowl Kurta","Kurta with Jacket Jeans","Dhoti with Shirt","Pathani with Nehru Jacket","Printed Nehru plus Trouser","Layered Kurta Set","Asymmetric Hem Kurta plus Pants","Bundi Jacket plus Kurta","Modern Dhoti Set","Kurta plus Denim Jacket","Fusion Bandhgala"],"Western":["Shirt plus Jeans","T-shirt plus Cargo","Blazer Set","Hoodie plus Jeans","Polo plus Chinos","Denim Jacket Set","Sweatshirt plus Joggers","Formal Shirt plus Trousers","Leather Jacket plus Jeans","Linen Shirt plus Shorts","Bomber Jacket plus Jeans","Oversized Tee plus Jeans","Checks Shirt plus Jeans","Henley plus Chinos","Varsity Jacket plus Cargo","Turtle Neck plus Trousers","Printed Shirt plus Shorts","Flannel Shirt plus Jeans","Suit Set","Cargo Pants plus Hoodie"]}
    idx=20
    for g,sdict in [("Female",styles_f),("Male",styles_m)]:
        for sty,dlist in sdict.items():
            for dtype in dlist:
                if not any(x["type"]==dtype for x in base):
                    base.append({"id":idx,"gender":g,"body":["Pear","Hourglass","Rectangle"] if g=="Female" else ["Trapezoid","Rectangle"],"skin":["Fair","Wheatish","Dusky","Deep"],"under":["Cool","Warm","Neutral"],"style":sty,"type":dtype,"season":[random.choice(["Summer","Winter","Monsoon","All Season"])],"occasion":[random.choice(["Office","Party","Wedding","Temple","College","Date","Casual Outing","Festive","Travel","Brunch"])],"name":dtype+" - Premium","color":random.choice(["Red","Blue","Black","White","Beige","Olive"]),"reason":dtype+" is trending"})
                    idx+=1
    return base,styles_f,styles_m

wardrobe,styles_f_main,styles_m_main=get_wardrobe()
st.sidebar.title("Your Profile")
user_name=st.sidebar.text_input("Name:",value="Aditi")
gender=st.sidebar.selectbox("Gender",["Female","Male"])
if gender=="Male" and st.session_state.sel_body in ["Pear","Hourglass","Apple"]: st.session_state.sel_body="Trapezoid"
if gender=="Female" and st.session_state.sel_body in ["Trapezoid","Oval","Triangle"]: st.session_state.sel_body="Pear"
opts=["Pear","Hourglass","Rectangle","Inverted Triangle","Apple"] if gender=="Female" else ["Trapezoid","Rectangle","Oval","Triangle","Inverted Triangle"]
for b in opts:
    if st.sidebar.button(b,key="b_"+b,use_container_width=True,type="primary" if st.session_state.sel_body==b else "secondary"): st.session_state.sel_body=b
body_shape=st.session_state.sel_body
for s in ["Fair","Wheatish","Dusky","Deep"]:
    if st.sidebar.button(s,key="s_"+s,use_container_width=True,type="primary" if st.session_state.sel_skin==s else "secondary"): st.session_state.sel_skin=s
skin_tone=st.session_state.sel_skin
for u in ["Cool","Warm","Neutral"]:
    if st.sidebar.button(u,key="u_"+u,use_container_width=True,type="primary" if st.session_state.sel_under==u else "secondary"): st.session_state.sel_under=u
undertone=st.session_state.sel_under
my_best_colors=smart_colors[skin_tone]
style=st.sidebar.selectbox("Style Category",["Traditional","Indo-Western","Western"])
type_map={"Female":styles_f_main,"Male":styles_m_main}
dress_type=st.sidebar.selectbox("Type (20 options)",type_map[gender][style])
season=st.sidebar.selectbox("Season",["Summer","Winter","Monsoon","Autumn","Spring","All Season"])
occasion=st.sidebar.selectbox("Occasion",["Office","Party","Wedding","Temple","College","Date","Casual Outing","Festive","Interview","Travel","Brunch","Everyday"])
find_btn=st.sidebar.button("Find My Perfect Dress",use_container_width=True,type="primary")
st.title("Hi "+user_name+"! Your Personal Stylist")
st.caption(f"Shape: {body_shape} | Skin: {skin_tone} | Gender: {gender}")
st.success(f"Best colours for {skin_tone}: {', '.join(my_best_colors)}")
c1,c2,c3=st.columns(3)
c1.markdown(f"<div class='green-box'><h4>What Suits You?</h4><p>{body_shape}</p></div>",unsafe_allow_html=True)
c2.markdown(f"<div class='pink-box'><h4>What to Avoid?</h4><p>Avoid oversized</p></div>",unsafe_allow_html=True)
c3.markdown(f"<div class='yellow-box'><h4>Best Colors</h4><p>{', '.join(my_best_colors)}</p></div>",unsafe_allow_html=True)
def score_dress(d):
    s=0
    if d["gender"]==gender: s+=2
    if body_shape in d["body"]: s+=2
    if skin_tone in d["skin"]: s+=1
    if d["style"]==style: s+=2
    if d["type"]==dress_type: s+=3
    return s
tab1,tab2,tab3=st.tabs(["AI Suggestions","Full Almira View","My Wishlist"])
with tab1:
    if find_btn:
        scored=sorted(wardrobe,key=lambda x:score_dress(x),reverse=True)
        top2=scored[:2]
        cols=st.columns(2)
        for i,dress in enumerate(top2):
            with cols[i]:
                st.markdown(f"<div class='dress-card'><h3>{dress['name']}</h3><p>{dress['type']} | {dress['style']}<br>{dress['color']}</p></div>",unsafe_allow_html=True)
                if st.button(f"Add {dress['id']}",key=f"w_{dress['id']}"):
                    if dress not in st.session_state.wishlist: st.session_state.wishlist.append(dress); st.toast("Added!")
    else: st.info("Click Find My Perfect Dress")
with tab2:
    st.subheader(f"Full Almira - {gender} | {style}")
    jewellery_f=["Jhumka Earrings","Choker Necklace","Bangles Set","Maang Tikka","Nath","Payal","Kamarbandh","Ring","Mangalsutra","Nose Pin"]
    footwear_f=["Kolhapuri Chappal","Jutti","Block Heels","Pencil Heels","Mojari","Sneakers","Wedges","Ballerina Flats","Boots","Stilettos"]
    jewellery_m=["Watch","Bracelet","Chain","Ring","Brooch","Kada","Stud Earrings","Locket","Cufflinks","Kalgi"]
    footwear_m=["Mojari","Kolhapuri Chappal","Formal Shoes","Sneakers","Loafers","Jutti","Boots","Sandals","Peshawari Chappal","Slip-on"]
    st.markdown("### Dress Collection")
    filt=[d for d in wardrobe if d["gender"]==gender and d["style"]==style]
    cols=st.columns(3)
    for idx,dress in enumerate(filt[:20]):
        with cols[idx - (idx//3)*3]:
            st.markdown(f"<div class='dress-card'><b>{dress['name']}</b><br>{dress['color']}</div>",unsafe_allow_html=True)
            if st.button("Add",key=f"alm_{dress['id']}_{style}"):
                if dress not in st.session_state.wishlist: st.session_state.wishlist.append(dress); st.toast("Added!")
    st.markdown(f"### Jewellery - For {gender}")
    j_list=jewellery_f if gender=="Female" else jewellery_m
    jcols=st.columns(4)
    for j_idx,j_name in enumerate(j_list):
        col_pos = j_idx - (j_idx//4)*4
        with jcols[col_pos]:
            st.markdown(f"<div class='dress-card'><b>{j_name}</b></div>",unsafe_allow_html=True)
            if st.button("Add J",key=f"jew_{j_idx}_{gender}_{style}"):
                st.session_state.wishlist.append({"name":j_name,"type":"Jewellery","color":"Gold","style":style})
                st.toast("Added!")
    st.markdown(f"### Footwear - For {gender}")
    f_list=footwear_f if gender=="Female" else footwear_m
    fcols=st.columns(4)
    for f_idx,f_name in enumerate(f_list):
        col_pos2 = f_idx - (f_idx//4)*4
        with fcols[col_pos2]:
            st.markdown(f"<div class='dress-card'><b>{f_name}</b></div>",unsafe_allow_html=True)
            if st.button("Add F",key=f"foot_{f_idx}_{gender}_{style}"):
                st.session_state.wishlist.append({"name":f_name,"type":"Footwear","color":"Black","style":style})
                st.toast("Added!")
with tab3:
    st.subheader(f"Wishlist - {len(st.session_state.wishlist)} items")
    if not st.session_state.wishlist: st.write("No items")
    else:
        for d in st.session_state.wishlist: st.write(f"✅ {d['name']}")
        if st.button("Clear Wishlist"): st.session_state.wishlist=[]; st.rerun()
