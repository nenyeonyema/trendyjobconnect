document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('.toggle-button');
    const mobileNav = document.querySelector('.mobile-nav');
    const closebar = document.querySelector('.closing-bar');

    const handleResize = () => {
        const viewportWidth = window.innerWidth;

        if (viewportWidth >= 768) {
            mobileNav.style.display = "none";
            closebar.style.display = "none";
            toggleButton.style.display = "flex";
        }
    };

    toggleButton.addEventListener('click', () => {
        let viewportWidth = window.innerWidth;

        if (viewportWidth < 768) {
            mobileNav.style.display = "block";
            closebar.style.display = "block";
            toggleButton.style.display = "none";
        }
    });

    closebar.addEventListener('click', () => {
        mobileNav.style.display = "none";
        closebar.style.display = "none";
        toggleButton.style.display = "flex";
    });

    window.addEventListener('resize', handleResize);
    handleResize();
});
