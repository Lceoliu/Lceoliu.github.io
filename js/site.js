(function () {
  function loadThreeSceneRuntime() {
    if (!document.querySelector('[data-three-scene]')) return;
    if (window.MyPageThreeSceneRuntimePromise) return;

    window.MyPageThreeSceneRuntimePromise = true;

    var script = document.createElement('script');
    script.src = '/js/three-scene.js';
    script.dataset.threeSceneRuntime = 'true';
    script.onerror = function () {
      console.error('Failed to load Three.js scene runtime.');
    };
    document.body.appendChild(script);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadThreeSceneRuntime, { once: true });
  } else {
    loadThreeSceneRuntime();
  }
})();
