import streamlit as st
import random
st.set_page_config(page_title="Smart Wardrobe AI Pro", page_icon="👗", layout="wide")
st.markdown("""
<style>
.green-box { background:#E8F5E9; border-radius:12px; padding:15px; border-left:5px solid #4CAF50; min-height:160px; }
.pink-box { background:#FCE4EC; border-radius:12px; padding:15px; border-left:5px solid #E91E63; min-height:160px; }
.yellow-box { background:#FFF9C4; border-radius:12px; padding:15px; border-left:5px solid #FFC107; min-height:160px; }
.dress-card { background:white; border-radius:12px; padding:15px; box-shadow:0 4px 12px rgba(0,0,0,0.15); text-align:center; margin-bottom:15px; border:1px solid #eee; }
.dress-card-match { background:#E8F5E9; border-radius:12px; padding:15px; box-shadow:0 4px 12px rgba(76,175,80,0.4); text-align:center; margin-bottom:15px; border:2px solid #4CAF50; }
.almira-box { background: linear-gradient(to bottom, #8B4513, #D2B48C); border:5px solid #5D4037; border-radius:15px; padding:20px; }
.skin-circle { width:50px; height:50px; border-radius:50%; border:3px solid #FFD700; display:inline-block; box-shadow:0 2px 5px rgba(0,0,0,0.3); }
.kurti-box { background:white; border-radius:12px; border:2px solid #FFD700; padding:5px; }
.color-dot { width:24px; height:24px; border-radius:50%; display:inline-block; margin:2px; border:2px solid white; box-shadow:0 0 4px #000; }
.color-badge { display:inline-block; padding:4px 8px; border-radius:15px; color:white; font-size:11px; font-weight:bold; margin:2px; }
</style>
""", unsafe_allow_html=True)

if 'wishlist' not in st.session_state: st.session_state.wishlist = []
if 'sel_body' not in st.session_state: st.session_state.sel_body = "Pear"
if 'sel_skin' not in st.session_state: st.session_state.sel_skin = "Wheatish"
if 'sel_under' not in st.session_state: st.session_state.sel_under = "Warm"

smart_colors = {"Fair": ["Pastel Pink", "Lavender", "Sky Blue", "Mint", "Beige"],"Wheatish": ["Mustard", "Olive", "Teal", "Rust", "Wine"],"Dusky": ["Royal Blue", "Emerald", "Wine", "Gold", "Red"],"Deep": ["Cobalt Blue", "Ruby Red", "Emerald", "Black", "White"]}
color_hex = {"Mustard":"#FFC107","Olive":"#808000","Teal":"#008080","Rust":"#B7410E","Wine":"#722F37","Royal Blue":"#4169E1","Emerald":"#50C878","Gold":"#FFD700","Red":"#E53935","Pastel Pink":"#FFB6C1","Lavender":"#E6E6FA","Sky Blue":"#87CEEB","Mint":"#98FB98","Beige":"#F5F5DC","Cobalt Blue":"#0047AB","Ruby Red":"#9B111E","Black":"#000000","White":"#FFFFFF"}

def get_wardrobe():
    base=[]
    base.append({"id":1,"gender":"Female","body":["Hourglass","Rectangle"],"skin":["Fair","Wheatish"],"under":["Cool","Neutral"],"style":"Traditional","type":"Saree - Silk","season":["Festive","Winter","All Season"],"occasion":["Wedding","Festive","Temple"],"name":"Royal Red Silk Saree","color":"Red & Gold","reason":"Perfect drape for Hourglass"})
    base.append({"id":2,"gender":"Female","body":["Pear","Apple"],"skin":["Wheatish","Dusky"],"under":["Warm","Neutral"],"style":"Traditional","type":"Anarkali Suit","season":["Summer","All Season"],"occasion":["Party","Festive","Temple"],"name":"Mustard Anarkali","color":"Mustard","reason":"Anarkali hides lower body"})
    base.append({"id":3,"gender":"Female","body":["Rectangle"],"skin":["Fair"],"under":["Cool"],"style":"Western","type":"Bodycon Dress","season":["Summer"],"occasion":["Party","Date"],"name":"Black Bodycon Dress","color":"Black","reason":"Creates curves"})
    base.append({"id":10,"gender":"Male","body":["Trapezoid","Rectangle"],"skin":["Wheatish","Dusky"],"under":["Warm","Neutral"],"style":"Traditional","type":"Kurta Pajama","season":["Festive","Winter"],"occasion":["Wedding","Festive","Temple"],"name":"White Chikankari Kurta","color":"White","reason":"Fitted kurta"})
    styles_f = {"Traditional":["Saree - Silk","Lehenga Choli","Salwar Kameez","Anarkali Suit","Sharara","Palazzo Suit","Kurta Palazzo","Banarasi Saree","Patiala Suit","Long Gown","Phulkari Suit","Chikankari Saree","Ghagra Choli","Chanderi Saree","Kanchipuram Saree","Sambalpuri Suit","Maheshwari Suit","Paithani Saree","Bandhani Saree","Kalamkari Anarkali"],"Indo-Western":["Dhoti + Crop Top","Palazzo Saree","Kurta with Jeans","Cape Lehenga","Jacket Lehenga","Saree with Belt","Dhoti Pants + Kurti","Sharara + Crop Top","Ruffle Saree","Co-ord Set","Kurta with Palazzo","Saree Gown","Dhoti Saree","Peplum with Sharara","Long Jacket with Lehenga","Drape Saree","Fusion Gown","Crop Top with Dhoti Skirt","Kurta Dress with Belt","Co-ord with Cape"],"Western":["Bodycon Dress","A-Line Dress","Maxi Dress","Jumpsuit","Skirt + Top","Blazer Dress","Shirt Dress","Midi Dress","Off-Shoulder Gown","Denim Dress","Peplum Dress","Culotte Jumpsuit","Slip Dress","Wrap Dress","Pencil Skirt + Blouse","Playsuit","Tunic Dress","Co-ord Blazer Set","Kimono Dress","Corset Top + Jeans"]}
    styles_m = {"Traditional":["Kurta Pajama","Sherwani","Dhoti Kurta","Pathani Suit","Bandhgala","Kurta + Nehru Jacket","Lungi + Shirt","Angarkha","Churidar Kurta","Modi Jacket","Kurta Dhoti","Achkan","Lungi Kurta","Peshawari Suit","Aligarhi Kurta","Mundu + Shirt","Jodhpuri Bandhgala","Embroidered Kurta","Sadri Jacket","Mysore Peta + Sherwani"],"Indo-Western":["Nehru Jacket + Kurta","Kurta + Jeans","Jodhpuri Suit","Short Kurta + Trouser","Bandhgala + Jeans","Kurta + Waistcoat","Indo-Western Sherwani","Printed Kurta Set","Asymmetric Kurta","Cowl Kurta","Kurta with Jacket Jeans","Dhoti with Shirt","Pathani with Nehru Jacket","Printed Nehru + Trouser","Layered Kurta Set","Asymmetric Hem Kurta + Pants","Bundi Jacket + Kurta","Modern Dhoti Set","Kurta + Denim Jacket","Fusion Bandhgala"],"Western":["Shirt + Jeans","T-shirt + Cargo","Blazer Set","Hoodie + Jeans","Polo + Chinos","Denim Jacket Set","Sweatshirt + Joggers","Formal Shirt + Trousers","Leather Jacket + Jeans","Linen Shirt + Shorts","Bomber Jacket + Jeans","Oversized Tee + Jeans","Checks Shirt + Jeans","Henley + Chinos","Varsity Jacket + Cargo","Turtle Neck + Trousers","Printed Shirt + Shorts","Flannel Shirt + Jeans","Suit Set","Cargo Pants + Hoodie"]}
    idx=20
    for g,sdict in [("Female",styles_f),("Male",styles_m)]:
        for sty,dlist in sdict.items():
            for dtype in dlist:
                if not any(x["type"]==dtype for x in base):
                    base.append({"id":idx,"gender":g,"body":["Pear","Hourglass","Rectangle"] if g=="Female" else ["Trapezoid","Rectangle"],"skin":["Fair","Wheatish","Dusky","Deep"],"under":["Cool","Warm","Neutral"],"style":sty,"type":dtype,"season":[random.choice(["Summer","Winter","Monsoon","All Season"])],"occasion":[random.choice(["Office","Party","Wedding","Temple","College","Date","Casual Outing","Festive","Travel","Brunch"])],"name":dtype+" - Premium","color":random.choice(["Red","Blue","Black","White","Beige","Olive"]),"reason":dtype+" is trending in "+sty+" for "+g})
                    idx+=1
    return base, styles_f, styles_m

wardrobe, styles_f_main, styles_m_main = get_wardrobe()
st.sidebar.title("Your Profile")
user_name = st.sidebar.text_input("Name:", value="Aditi")
gender = st.sidebar.selectbox("Gender", ["Female","Male"])
st.sidebar.markdown("**Select Body Shape:**")
st.sidebar.markdown('<div class="kurti-box"><svg viewBox="0 0 400 110" xmlns="http://www.w3.org/2000/svg"><g transform="translate(10,5)"><circle cx="40" cy="12" r="8" fill="none" stroke="black" stroke-width="1.3"/><path d="M20 22 Q40 28 60 22 L55 65 Q40 75 25 65 Z" fill="black"/><text x="18" y="100" font-size="9" font-weight="bold">Pear</text></g><g transform="translate(110,5)"><circle cx="40" cy="12" r="8" fill="none" stroke="black" stroke-width="1.3"/><path d="M20 22 Q40 28 60 22 L55 40 Q40 46 25 40 Z" fill="black"/><ellipse cx="40" cy="55" rx="12" ry="4" fill="none" stroke="#FFD700" stroke-width="3"/><text x="5" y="100" font-size="9" font-weight="bold">Hourglass</text></g><g transform="translate(210,5)"><circle cx="40" cy="12" r="8" fill="none" stroke="black" stroke-width="1.3"/><path d="M20 22 L60 22 L60 70 L20 70 Z" fill="black"/><text x="8" y="100" font-size="9" font-weight="bold">Rectangle</text></g><g transform="translate(310,5)"><circle cx="40" cy="12" r="8" fill="none" stroke="black" stroke-width="1.3"/><path d="M15 22 Q40 28 65 22 L55 65 Q40 70 25 65 Z" fill="black"/><text x="0" y="100" font-size="7" font-weight="bold">Inv Tri</text></g></svg></div>', unsafe_allow_html=True)
opts = ["Pear","Hourglass","Rectangle","Inverted Triangle","Apple"] if gender=="Female" else ["Trapezoid","Rectangle","Oval","Triangle","Inverted Triangle"]
for b in opts:
    if st.sidebar.button(b, key="b_"+b, use_container_width=True, type="primary" if st.session_state.sel_body==b else "secondary"):
        st.session_state.sel_body=b
body_shape=st.session_state.sel_body
st.sidebar.markdown("**Select Skin Tone:**")
st.sidebar.markdown('<div style="background:white; border-radius:12px; border:2px solid #FFD700; padding:10px; text-align:center;"><div style="display:inline-block; text-align:center; margin:5px;"><div class="skin-circle" style="background:#F8D5C2;"></div><br><b style="font-size:10px;">Fair</b></div><div style="display:inline-block; text-align:center; margin:5px;"><div class="skin-circle" style="background:#E5B08D;"></div><br><b style="font-size:10px;">Wheatish</b></div><div style="display:inline-block; text-align:center; margin:5px;"><div class="skin-circle" style="background:#C6866A;"></div><br><b style="font-size:10px;">Dusky</b></div><div style="display:inline-block; text-align:center; margin:5px;"><div class="skin-circle" style="background:#8D5524;"></div><br><b style="font-size:10px;">Deep</b></div></div>', unsafe_allow_html=True)
for s in ["Fair","Wheatish","Dusky","Deep"]:
    if st.sidebar.button(s, key="s_"+s, use_container_width=True, type="primary" if st.session_state.sel_skin==s else "secondary"):
        st.session_state.sel_skin=s
skin_tone=st.session_state.sel_skin
st.sidebar.markdown("**Undertone:**")
for u in ["Cool","Warm","Neutral"]:
    if st.sidebar.button(u, key="u_"+u, use_container_width=True, type="primary" if st.session_state.sel_under==u else "secondary"):
        st.session_state.sel_under=u
undertone=st.session_state.sel_under
my_best_colors = smart_colors[skin_tone]
color_badge_html = ""
for col in my_best_colors:
    hexc = color_hex.get(col, "#888")
    color_badge_html += "<span class='color-badge' style='background:"+hexc+";'>"+col+"</span>"
st.sidebar.markdown("** "+skin_tone+" sathi 100% Match Colours:**")
st.sidebar.markdown(color_badge_html, unsafe_allow_html=True)
style=st.sidebar.selectbox("5. Style Category", ["Traditional","Indo-Western","Western"])
type_map = {"Female": styles_f_main, "Male": styles_m_main}
dress_type=st.sidebar.selectbox("6. "+style+" Type (20 options)", type_map[gender][style])
season=st.sidebar.selectbox("7. Season", ["Summer","Winter","Monsoon","Autumn","Spring","All Season"])
occasion=st.sidebar.selectbox("8. Place / Occasion (10+)", ["Office","Party","Wedding","Temple","College","Date","Casual Outing","Festive","Interview","Travel","Brunch","Everyday"])
find_btn=st.sidebar.button("Find My Perfect Dress", use_container_width=True, type="primary")
st.sidebar.info("BCA Final Year Project - SmartWardrobe AI")
suit_dict={"Pear":"A-line Kurta, Wide Palazzo","Hourglass":"Bodycon Dress, Silk Saree","Rectangle":"Ruffle Top, Peplum Kurta","Apple":"Empire Waist Kurta","Inverted Triangle":"Flared Bottom","Trapezoid":"Fitted Kurta","Oval":"Oversized Shirt","Triangle":"Layered Top"}
avoid_dict={"Pear":"Avoid tight bottoms","Hourglass":"Avoid oversized","Rectangle":"Avoid boxy cuts","Apple":"Avoid tight belt","Inverted Triangle":"Avoid puffy sleeves","Trapezoid":"Avoid baggy","Oval":"Avoid tight t-shirt","Triangle":"Avoid tight chest"}
color_dict={"Fair":"Pastel Pink, Lavender","Wheatish":"Mustard, Olive, Teal - Best Indian tone!","Dusky":"Royal Blue, Emerald","Deep":"Cobalt Blue, Ruby Red"}
why_dict={"Pear":"bright on top for balance","Hourglass":"Define waist","Rectangle":"Use belt","Apple":"V-neck slim look"}
suit_text=suit_dict.get(body_shape,"Stylish Co-ord")
avoid_text=avoid_dict.get(body_shape,"Avoid oversized")
color_text=color_dict.get(skin_tone,"Red Blue")
why_text=why_dict.get(body_shape,"Perfect for body balance")
st.title("Hi "+user_name+"! Your Personal Stylist")
st.caption("Your Shape: "+body_shape+" | Skin Tone: "+skin_tone+" | Gender: "+gender+" | Undertone: "+undertone)
st.success("Tujhya "+skin_tone+" skin tone sathi best 5 colours: "+ ", ".join(my_best_colors))
col1,col2,col3=st.columns(3)
col1.markdown("<div class='green-box'><h4>What Suits You?</h4><p>"+suit_text+"</p><p><i>Why? "+why_text+"</i></p></div>", unsafe_allow_html=True)
col2.markdown("<div class='pink-box'><h4>What to Avoid?</h4><p>"+avoid_text+"</p></div>", unsafe_allow_html=True)
col3.markdown("<div class='yellow-box'><h4>Best Colors For You</h4><p>"+color_text+"</p></div>", unsafe_allow_html=True)
st.divider()
def score_dress(d):
    s=0
    if d["gender"]==gender: s+=2
    if body_shape in d["body"]: s+=2
    if skin_tone in d["skin"]: s+=1
    if undertone in d["under"]: s+=1
    if d["style"]==style: s+=2
    if d["type"]==dress_type: s+=3
    if season in d["season"] or "All Season" in d["season"]: s+=1
    if occasion in d["occasion"]: s+=2
    if any(c.lower() in d["color"].lower() for c in my_best_colors): s+=3
    return s
tab1,tab2,tab3=st.tabs(["AI Suggestions","Full Almira View","My Wishlist"])
with tab1:
    if find_btn:
        scored=sorted(wardrobe, key=lambda x: score_dress(x), reverse=True)
        top2=scored[:2]
        cols=st.columns(2)
        for i,dress in enumerate(top2):
            with cols[i]:
                is_match = any(c.lower() in dress["color"].lower() for c in my_best_colors)
                card_class = "dress-card-match" if is_match else "dress-card"
                match_txt = "100% Match" if is_match else ""
                st.markdown("<div class='"+card_class+"'><h3>"+dress["name"]+"</h3><p>"+dress["type"]+" | "+dress["style"]+"<br>"+dress["color"]+" "+match_txt+"</p></div>", unsafe_allow_html=True)
                st.success("Why? Body "+body_shape+": "+dress["reason"])
                if st.button("Add to Wishlist "+str(dress["id"]), key="w_"+str(dress["id"])):
                    if dress not in st.session_state.wishlist:
                        st.session_state.wishlist.append(dress)
                        st.toast("Added!")
    else:
        st.info("Select from sidebar and click Find My Perfect Dress")
with tab2:
    st.subheader("Full Almira - "+gender+" | "+style+" - 20 Dresses + Jewellery + Footwear")
    st.markdown('<div class="almira-box"><h3 style="text-align:center; color:white;">My Wooden Almira - '+style+' Collection</h3><p style="text-align:center; color:#FFEB3B;">Dresses (20) + Jewellery (10) + Footwear (10) = 40 Items</p></div>', unsafe_allow_html=True)
    jewellery_f = ["Jhumka Earrings - Gold","Choker Necklace","Bangles Set - Red","Maang Tikka","Nath - Maharashtrian","Payal - Anklets","Kamarbandh","Ring - Cocktail","Mangalsutra - Modern","Nose Pin"]
    footwear_f = ["Kolhapuri Chappal","Jutti - Embroidered","Block Heels","Pencil Heels","Mojari - Traditional","Sneakers - White","Wedges","Ballerina Flats","Boots - Ankle","Stilettos"]
    jewellery_m = ["Watch - Titan","Bracelet - Leather","Chain - Gold","Ring - Silver","Brooch - Sherwani","Kada - Silver","Earrings - Stud","Locket","Cufflinks","Kalgi - Turban"]
    footwear_m = ["Mojari - Rajasthani","Kolhapuri Chappal","Formal Shoes - Black","Sneakers - White","Loafers","Jutti - Punjabi","Boots - Leather","Sandals","Peshawari Chappal","Slip-on Shoes"]
    st.info("Tu "+skin_tone+" select kela aahes: "+ ", ".join(my_best_colors))
    st.markdown("### 1. Dress Collection - 20 Items")
    filt=[d for d in wardrobe if d["gender"]==gender and d["style"]==style]
    cols=st.columns(3)
    for idx,dress in enumerate(filt[:20]):
        with cols[idx%3]:
            is_match = any(c.lower() in dress["color"].lower() for c in my_best_colors)
            card_class = "dress-card-match" if is_match else "dress-card"
            match_label = "100% Match for "+skin_tone if is_match else ""
            st.markdown("<div class='"+card_class+"'><b>"+dress["name"]+"</b><br><small>"+dress["type"]+"</small><br>"+dress["color"]+"<br>"+match_label+"</div>", unsafe_allow_html=True)
            c_cols = st.columns(5)
            for ci, col_name in enumerate(my_best_colors):
                hexc = color_hex.get(col_name, "#888888")
                with c_cols[ci]:
                    st.markdown("<div class='color-dot' style='background:"+hexc+";'></div><br><small>"+col_name[:3]+"</small>", unsafe_allow_html=True)
                    if st.button(col_name[:3], key="col_"+str(dress["id"])+"_"+str(ci)+"_"+skin_tone+"_"+style):
                        new_dress = dress.copy()
                        new_dress["id"] = dress["id"]*100 + ci
                        new_dress["color"] = col_name
                        new_dress["name"] = dress["type"]+" - "+col_name
                        if new_dress not in st.session_state.wishlist:
                            st.session_state.wishlist.append(new_dress)
                            st.toast(col_name+" Added!")
            if st.button("Add to Wishlist", key="alm_"+str(dress["id"])+"_"+skin_tone+"_"+style):
                if dress not in st.session_state.wishlist:
                    st.session_state.wishlist.append(dress)
                    st.toast("Added!")
            st.divider()
    st.markdown("### 2. Jewellery Collection - For "+gender+" - 10 Items")
    j_list = jewellery_f if gender=="Female" else jewellery_m
    j_cols = st.columns(4)
    for j_idx, j_name in enumerate(j_list[:10]):
        with j_cols[j_idx%4]:
            st.markdown("<div class='dress-card'><b>"+j_name+"</b><br><small>Matches with "+style+" Wear</small><br>Gold/ Silver<br><small>For "+occasion+"</small></div>", unsafe_allow_html=True)
            if st.button("Add Jewellery", key="jew_"+str(j_idx)+"_"+gender+"_"+style):
                st.session_state.wishlist.append({"name": j_name, "type": "Jewellery", "color": "Gold", "style": style, "occasion":[occasion], "season":[season]})
                st.toast(j_name+" Added!")
    st.divider()
    st.markdown("### 3. Footwear Collection - For "+gender+" - 10 Items")
    f_list = footwear_f if gender=="Female" else footwear_m
    f_cols = st.columns(4)
    for f_idx, f_name in enumerate(f_list[:10]):
        with f_cols[f_idx%4]:
            chosen_color = random.choice(my_best_colors)
            st.markdown("<div class='dress-card'><b>"+f_name+"</b><br><small>Comfort + Style</small><br>"+chosen_color+"<br><small>For "+season+"</small></div>", unsafe_allow_html=True)
            if st.button("Add Footwear", key="foot_"+str(f_idx)+"_"+gender+"_"+style):
                st.session_state.wishlist.append({"name": f_name, "type": "Footwear", "color": chosen_color, "style": style, "occasion":[occasion], "season":[season]})
                st.toast(f_name+" Added!")
with tab3:
    st.subheader("Wishlist - "+str(len(st.session_state.wishlist))+" items")
    if not st.session_state.wishlist:
        st.write("No items added yet")
    else:
        for d in st.session_state.wishlist:
            st.write("✅ "+d["name"]+" - "+d.get("type","Dress")+" ("+d.get("color","")+")")
        if st.button("Clear Wishlist"):
            st.session_state.wishlist=[]
            st.rerun()