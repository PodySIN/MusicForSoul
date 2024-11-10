/Комментарии*/
var LoopButton = document.getElementById('loopButton');
var LikeButton = document.getElementById('likeButton');
var CatalogAudio_mini = document.getElementById('CatalogAudio-mini')
var array_of_loops_buttons = null
var Audios_len = document.getElementsByClassName('MyMainAudio').length;
var Mini_audio_playing = 0
var Music_id_Playing = 0
var MiniPlayerStartPlaying = 0
var something_playing = 0
var auto_pause = false
var Absolute_Audios_Len = document.getElementById('MusicImageMini').name


window.onload = function() {
    LoadMiniPlayer();
};
function LoadMiniPlayer(){
    document.getElementById('ref_title').text = localStorage.getItem("TitleOfMiniPlayer")

    url_title = console.log(localStorage.getItem("TitleOfMiniPlayerHref"))
    console.log(url_title)
    document.getElementById('ref_title').href = url_title
    document.getElementById('ref_author').text = localStorage.getItem("AuthorOfMiniPlayer")
    document.getElementById('MusicImageMini').src = localStorage.getItem("ImageOfMiniPlayer")
    document.getElementById('SorceCatalogAudio-mini').src = localStorage.getItem("AudioOfMiniPlayer")
    CatalogAudio_mini.currentTime = localStorage.getItem("CurTimeOnMiniPlayer")
    CatalogAudio_mini.loop = localStorage.getItem("LoopOfMiniPlayer")
    CatalogAudio_mini.muted = !localStorage.getItem("MiniPlayerMuted")
    CatalogAudio_mini.volume = localStorage.getItem("VolumeOfMiniPlayer")
    console.log(CatalogAudio_mini)
    CatalogAudio_mini.load()

}
const interval = setInterval(() => {
    if (CatalogAudio_mini.readyState == 4){
        CatalogAudio_mini.play()
        if (MiniPlayerStartPlaying == 1){
            clearInterval(interval)
        }
    }
}, 1000)
function loop(_this) {
    let MiniAudio = document.getElementById('CatalogAudio-mini')
    let MiniLoopButton = document.getElementById('loopButtonMini')
    var values = _this.value.split('_')
    var val = values[0]
    var Len = values[1]
    if (array_of_loops_buttons == null){
        array_of_loops_buttons = new Array(Number(Len)).fill(0);
    }
    var ind = Number(val) - 1
    var MainAudio = document.getElementById('CatalogAudio' + val);
    if (array_of_loops_buttons[ind] == 0){
       _this.style.background = "#80002a";
       MiniLoopButton.style.background = "#80002a";
       MainAudio.loop = true
       MiniAudio.loop = true
       array_of_loops_buttons[ind] = 1
    }
    else{
        _this.style.background = "#e91e63";
        MiniLoopButton.style.background = "#e91e63";
        MainAudio.loop = false
        MiniAudio.loop = false
        array_of_loops_buttons[ind] = 0
    }
}
var MiniLoop = false
function loopmini(_this) {
    MiniLoop = !MiniLoop
    localStorage.setItem("LoopOfMiniPlayer", MiniLoop)
    var values = _this.value.split('_')
    var val = values[0]
    var Len = values[1]
    var ind = Number(val) - 1
    var MainAudio = document.getElementById('CatalogAudio' + val);
    let MiniAudio = document.getElementById('CatalogAudio-mini')
    TargetButton = document.getElementsByName(val)[0]
    if (array_of_loops_buttons == null){
        array_of_loops_buttons = new Array(Number(Len)).fill(0);
    }
    if (TargetButton != null){
        if (array_of_loops_buttons[ind] == 0){
           _this.style.background = "#80002a";
           TargetButton.style.background = "#80002a";
           MainAudio.loop = true
           MiniAudio.loop = true
           array_of_loops_buttons[ind] = 1
        }
        else{
            _this.style.background = "#e91e63";
            TargetButton.style.background = "#e91e63";
            MainAudio.loop = false
            MiniAudio.loop = false
            array_of_loops_buttons[ind] = 0
        }
    }
    else{
        if (array_of_loops_buttons[ind] == 0){
           _this.style.background = "#80002a";
           MiniAudio.loop = true
           array_of_loops_buttons[ind] = 1
        }
        else{
            _this.style.background = "#e91e63";
            MiniAudio.loop = false
            array_of_loops_buttons[ind] = 0
        }
        }
}
/возникает при конце Audio*/
function AudioEnd(val,Len) {
    if (array_of_loops_buttons == null){
        array_of_loops_buttons = new Array(Number(Len)).fill(0);
    }
    var ind = Number(val) - 1
    if (array_of_loops_buttons[ind] == 0){
        if (val != Len){
            let next_audio = document.getElementById('CatalogAudio' + (Number(val)+1).toString())
            next_audio.play()
        }
        else{
            let next_audio = document.getElementById('CatalogAudio1')
            next_audio.play()
        }
    }
}

/если пользователь лайкнул трек*/
function like(_this) {
    values = _this.value;
    values = values.split('_')
    val = values[0]
    func = values[1]
    request = new XMLHttpRequest()
    href = window.location.href
    href = href.slice(href.indexOf('M'), href.length)
    request.open("GET", 'http://127.0.0.1:8000/MusicForSoulCatalog/service/'+"?music_id=" + val, true);
    request.send();

    if (func == "like") {
        let heart = _this.querySelector('#heart')
        heart.style.color = "red";
        _this.value = val+'_unlike'
        heart.id = 'heart-liked'
    }
    else{
        let heart = _this.querySelector('#heart-liked')
        heart.style.color = "";
        _this.value = val+'_like'
        heart.id = 'heart'
    }
}
/stop и play у audio*/
const audios = document.querySelectorAll('.MyMainAudio');
CatalogAudio_mini.addEventListener('play', function() {
        FirstPlay()
        audios.forEach(otherAudio => {
            if (otherAudio !== audio) {
                Mini_audio_playing = 1
            }
        });
    });
function FirstPlay(){
MiniPlayerStartPlaying = 1
}
CatalogAudio_mini.addEventListener('pause', function() {
        audios.forEach(otherAudio => {
            if (otherAudio !== audio) {
                StopMini()
                Mini_audio_playing = 0
            }
        });
    });
function StopMini(){
    localStorage.setItem("CurTimeOnMiniPlayer", CatalogAudio_mini.currentTime)
}
audios.forEach(audio => {
    let i = audio.id.slice(12, audio.length)
    audio.addEventListener('play', function() {
        audios.forEach(otherAudio => {
            if (otherAudio !== audio) {
                something_playing = 0
                otherAudio.pause();
            }
        });
    });
});
for (let i = 1; i <= Absolute_Audios_Len; i++) {
    var audio = document.getElementById('CatalogAudio' + i.toString());
    if (audio){
        audio.addEventListener('play', function() {
            onAudioPlay(i);
        });
        audio.addEventListener('pause', function() {
            onAudioPause(i);
        });
    }
    else{
    }

}

function onAudioPlay(i) {
    let val = i.toString()
    let TargetAudio = document.getElementById('CatalogAudio'+val)
    document.getElementById('ref_title').text = document.getElementById('MusicRefTitle'+val).text
    document.getElementById('ref_author').text = document.getElementById('MusicRefAuthor'+val).text
    CatalogAudio_mini.muted = TargetAudio.muted
    TargetAudio.addEventListener('volumechange', function(){syncVolume(TargetAudio, CatalogAudio_mini)});
    CatalogAudio_mini.addEventListener('volumechange', function(){syncVolume(CatalogAudio_mini, TargetAudio)});
    if (Mini_audio_playing == 1 && Music_id_Playing == i){
        let CurTimeOnMiniPlayer = CatalogAudio_mini.currentTime
        localStorage.setItem("CurTimeOnMiniPlayer", CatalogAudio_mini.currentTime)
    }
    else{
        document.getElementById('ref_title').href = document.getElementById('MusicRefTitle'+val).getAttribute('href')
        document.getElementById('ref_author').href = document.getElementById('MusicRefAuthor'+val).getAttribute('href')
        let CatalogAudioHref = decodeURI(document.getElementById('SourceCatalogAudio'+val).src)
        CatalogAudioHref = decodeURIComponent('/' + CatalogAudioHref.slice(CatalogAudioHref.indexOf('media'), CatalogAudioHref.length))
        document.getElementById('SorceCatalogAudio-mini').src = CatalogAudioHref
        let CatalogImageHref = decodeURI(document.getElementById('MusicImage'+val).src)
        CatalogImageHref = decodeURIComponent('/' + CatalogImageHref.slice(CatalogImageHref.indexOf('media'), CatalogImageHref.length))
        let MusicImage = document.getElementById('MusicImageMini')
        MusicImage.src = CatalogImageHref
        CatalogAudio_mini.load()
        let LoopMiniButton = document.getElementById('loopButtonMini')
        LoopMiniButton.value = val + '_' + Audios_len.toString()
    }
    if (Mini_audio_playing == 0 && Music_id_Playing == i){
    console.log('иии')
        Music_id_Playing = i
        TargetAudio.pause()
        TargetAudio.currentTime = localStorage.getItem("CurTimeOnMiniPlayer")
        CatalogAudio_mini.currentTime = localStorage.getItem("CurTimeOnMiniPlayer")
        CatalogAudio_mini.play()

    }
    else if (Mini_audio_playing == 0 && Music_id_Playing != i){
        localStorage.setItem("CurTimeOnMiniPlayer", 0)
        Music_id_Playing = i
        TargetAudio.pause()
        CatalogAudio_mini.play()
    }
    else if (Mini_audio_playing == 1 && Music_id_Playing == i){
        console.log('zzz')
        TargetAudio.pause()
        CatalogAudio_mini.pause()
        Mini_audio_playing = 0
    }
    else{
        console.log('b')
        TargetAudio.pause()
        CatalogAudio_mini.play()
        Music_id_Playing = i
    }

    TitleRefForStorage = "{% url \'Cur_music\' music_id=" + val +" %}"
    AuthorRefForStorage = "{% url \'Cur_author\' author_id="+"3"+" %}"
    localStorage.setItem("ImageOfMiniPlayer", document.getElementById('MusicImageMini').src)
    localStorage.setItem("AudioOfMiniPlayer",document.getElementById('SorceCatalogAudio-mini').src)
    localStorage.setItem("TitleOfMiniPlayer", document.getElementById('ref_title').text)
    localStorage.setItem("TitleOfMiniPlayerHref", TitleRefForStorage)
    localStorage.setItem("AuthorOfMiniPlayerHref", AuthorRefForStorage)
}

function onAudioPause(i) {
    console.log('stop')

}

function syncVolume(sourceAudio, targetAudio) {
    if (targetAudio.muted || sourceAudio.muted){
        targetAudio.muted = sourceAudio.muted;
        localStorage.setItem("MiniPlayerMuted", targetAudio.muted)
    }
    else{
        targetAudio.volume = sourceAudio.volume;
        localStorage.setItem("VolumeOfMiniPlayer", targetAudio.volume)

    }
}

function MiniAudioEnd(){
    if (Music_id_Playing == Audios_len){
        NextAudio = document.getElementById('CatalogAudio1')
    }
    else{
        NextAudio = document.getElementById('CatalogAudio'+(Music_id_Playing+1).toString())
    }
    NextAudio.play()
}
